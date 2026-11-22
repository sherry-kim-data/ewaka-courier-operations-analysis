"""
Weekday x hour order forecast for eWAKA time-block slots.

Demand    : every order offer in the history file (incl. ones couriers missed or rejected),
            1 May - 31 Aug 2026 (current motorbike fleet). Hours are Nairobi local time (+03:00).
Forecast  : per weekday x hour cell, a blend of
              (a) the cell's own weekly mean, and
              (b) smoothed = weekday's mean daily total x share of daily orders in that hour
            weighted n/(n+K) toward (a), n = weeks observed.
Range     : P10 / P90 of the cell's weekly counts.
Slots     : ceil(forecast x (1 + BUFFER) / CAP); 0 when forecast < MIN_ORDERS.
            CAP = finished orders per courier online hour in the same window (performance file).
Backtest  : fit May-Jul, forecast August; compare with naive "same weekday-hour last week".

Self-contained: Python 3.7+ standard library only, no other scripts needed.
Put this file in the same folder as:
    boltsend_rider_history.xlsx      (required)
    boltsend_rider_perfomance.xlsx   (optional; used to measure CAP, else CAP_FALLBACK)
Usage: python3 demand_forecast.py
Output: printed tables + demand_forecast.csv (written next to this script)
"""
import csv
import math
import sys
import xml.etree.ElementTree as ET
import zipfile
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
HISTORY = HERE / "boltsend_rider_history.xlsx"
PERF = HERE / "boltsend_rider_perfomance.xlsx"
CAP_FALLBACK = 1.5  # orders per courier-hour used when the performance file is absent
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


# ---------------- minimal .xlsx reader (first sheet, header row -> dicts) ----------------
def load_rows(path):
    with zipfile.ZipFile(path) as z:
        shared = []
        if "xl/sharedStrings.xml" in z.namelist():
            root = ET.fromstring(z.read("xl/sharedStrings.xml"))
            shared = ["".join(t.text or "" for t in si.iter(f"{{{NS['m']}}}t"))
                      for si in root.findall("m:si", NS)]
        header, rows = None, []
        with z.open("xl/worksheets/sheet1.xml") as f:
            for _, el in ET.iterparse(f):
                if el.tag != f"{{{NS['m']}}}row":
                    continue
                cells = {}
                for c in el.findall("m:c", NS):
                    col = "".join(ch for ch in c.get("r") if ch.isalpha())
                    v = c.find("m:v", NS)
                    if c.get("t") == "s" and v is not None:
                        cells[col] = shared[int(v.text)]
                    else:
                        cells[col] = v.text if v is not None else None
                el.clear()
                if header is None:
                    header = cells
                else:
                    rows.append({header[k]: v for k, v in cells.items() if k in header})
    return rows


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def excel_date(serial):
    return (date(1899, 12, 30) + timedelta(days=int(serial))).isoformat()
START, END = date(2026, 5, 1), date(2026, 8, 31)
BACKTEST_SPLIT = date(2026, 8, 1)
K = 8              # shrinkage strength (weeks) toward the smoothed weekday x hour-share estimate
BUFFER = 0.15      # extra slot headroom
MIN_ORDERS = 0.5   # below this forecast an hour gets no slots
CAP = None         # orders one courier handles per hour; None = measure from performance file
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
NIGHT = range(0, 6)  # folded into one "00-05" row in the printed grids


def daterange(a, b):
    while a <= b:
        yield a
        a += timedelta(days=1)


def hourly_counts(rows):
    """(date, hour) -> offers."""
    c = defaultdict(int)
    for r in rows:
        day = date.fromisoformat(r["date"][:10])
        if START <= day <= END:
            c[(day, int(r["date"][11:13]))] += 1
    return c


def measure_cap(perf_rows):
    on = fin = 0.0
    for r in perf_rows:
        if START <= date.fromisoformat(excel_date(float(r["report_date"]))) <= END:
            on += num(r["online_time_min"]) or 0
            fin += num(r["finished_rides"]) or 0
    return fin / (on / 60)


def pctl(xs, q):
    xs = sorted(xs)
    i = q * (len(xs) - 1)
    lo = math.floor(i)
    return xs[lo] + (xs[min(lo + 1, len(xs) - 1)] - xs[lo]) * (i - lo)


def fit(counts, a, b):
    """Forecast dict (weekday, hour) -> (forecast, p10, p90, n) from dates a..b."""
    samples = defaultdict(list)            # (wd, h) -> weekly counts
    daily = defaultdict(list)              # wd -> daily totals
    hour_tot = [0] * 24
    for day in daterange(a, b):
        wd = day.weekday()
        tot = 0
        for h in range(24):
            v = counts.get((day, h), 0)
            samples[(wd, h)].append(v)
            hour_tot[h] += v
            tot += v
        daily[wd].append(tot)
    share = [x / sum(hour_tot) for x in hour_tot]
    out = {}
    for wd in range(7):
        day_mean = sum(daily[wd]) / len(daily[wd])
        for h in range(24):
            s = samples[(wd, h)]
            n = len(s)
            w = n / (n + K)
            f = w * (sum(s) / n) + (1 - w) * day_mean * share[h]
            out[(wd, h)] = (f, pctl(s, 0.10), pctl(s, 0.90), n)
    return out


def slots(f, cap):
    return 0 if f < MIN_ORDERS else math.ceil(f * (1 + BUFFER) / cap)


def backtest(counts):
    fc = fit(counts, START, BACKTEST_SPLIT - timedelta(days=1))
    e_cell = e_naive = e_day = e_day_naive = 0.0
    n_cell = n_day = 0
    for day in daterange(BACKTEST_SPLIT, END):
        wd, prev = day.weekday(), day - timedelta(days=7)
        dt = dp = dn = 0
        for h in range(24):
            act = counts.get((day, h), 0)
            pred, naive = fc[(wd, h)][0], counts.get((prev, h), 0)
            e_cell += abs(act - pred)
            e_naive += abs(act - naive)
            n_cell += 1
            dt, dp, dn = dt + act, dp + pred, dn + naive
        e_day += abs(dt - dp)
        e_day_naive += abs(dt - dn)
        n_day += 1
    return {"cell_mae": e_cell / n_cell, "cell_mae_naive": e_naive / n_cell,
            "day_mae": e_day / n_day, "day_mae_naive": e_day_naive / n_day, "days": n_day}


def grid(title, fc, cell, total, fmt):
    print(f"\n{title}")
    print("Hour   " + "".join(f"{d:>7}" for d in DAYS) + "    Avg")
    rows = [("00-05", list(NIGHT))] + [(f"{h:02d}:00", [h]) for h in range(6, 24)]
    for lab, hs in rows:
        vals = [sum(cell(fc[(wd, h)]) for h in hs) for wd in range(7)]
        print(f"{lab:6} " + "".join(fmt(v).rjust(7) for v in vals) + fmt(sum(vals) / 7).rjust(7))
    tots = [sum(cell(fc[(wd, h)]) for h in range(24)) for wd in range(7)]
    print("-" * 63)
    print(f"{total:6} " + "".join(fmt(v).rjust(7) for v in tots) + fmt(sum(tots) / 7).rjust(7))


def main():
    if not HISTORY.exists():
        sys.exit(f"Missing {HISTORY.name}. Put it in the same folder as this script: {HERE}")
    counts = hourly_counts(load_rows(HISTORY))
    if CAP:
        cap = CAP
    elif PERF.exists():
        cap = measure_cap(load_rows(PERF))
    else:
        cap = CAP_FALLBACK
        print(f"Note: {PERF.name} not found, using {CAP_FALLBACK} orders per courier-hour.")
    fc = fit(counts, START, END)
    n_days = (END - START).days + 1
    observed = sum(counts.values())

    print(f"Window {START} .. {END}: {observed:,} offers over {n_days} days ({observed / n_days:.1f}/day)")
    print(f"Capacity: {cap:.2f} orders per courier-hour | buffer {BUFFER:.0%} | min {MIN_ORDERS} orders for a slot")

    grid("FORECAST ORDERS (offers) per hour", fc, lambda x: x[0], "Day", lambda v: f"{v:.1f}")
    grid("SUGGESTED TIME-BLOCK SLOTS: couriers to book in each hour\n"
         "(00-05 row and bottom row are sums of hourly slots = courier-hours)",
         fc, lambda x: slots(x[0], cap), "C-hrs", lambda v: f"{v:.0f}")

    bt = backtest(counts)
    print(f"\nBACKTEST (fit May-Jul, forecast {bt['days']} August days)")
    print(f"  per hour-cell MAE: {bt['cell_mae']:.2f} orders  (naive last-week {bt['cell_mae_naive']:.2f})")
    print(f"  per day MAE:       {bt['day_mae']:.1f} orders  (naive last-week {bt['day_mae_naive']:.1f})")

    weekly_fc = sum(v[0] for v in fc.values())
    print(f"\nCheck: forecast {weekly_fc:.0f} offers/week vs observed {observed / n_days * 7:.0f}/week")
    print("\nCaveats: offers only count orders sent to this fleet (true demand may be higher when couriers were short);"
          "\n17 weeks of data has no seasonality or holidays, so re-run monthly; CAP is an all-hours average,"
          "\nso peak-hour slots err on the generous side.")

    out = HERE / "demand_forecast.csv"
    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["weekday", "hour", "forecast_orders", "low_p10", "high_p90", "weeks_observed", "slots"])
        for wd in range(7):
            for h in range(24):
                x = fc[(wd, h)]
                w.writerow([DAYS[wd], f"{h:02d}:00", round(x[0], 2), round(x[1], 1), round(x[2], 1), x[3], slots(x[0], cap)])
    print(f"\nwrote {out.name} (168 rows)")


if __name__ == "__main__":
    main()
