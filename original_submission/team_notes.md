# SCU × eWAKA · MSBA Analytics Showdown · Fall 2026: Full Overview

**Team 7:** Sinhye Kim · Yan Wu · Wei-Chia Lin · Ethan Casey
**Deck:** BoltSend_eWAKA_courier_performance.pptx (21 main slides + appendix A1–A6)
**Speaking split:** Yan 1–5 · Vivien 6–9 · Sherry 10–15 · Ethan 16–21

**The big idea:** When couriers win, eWAKA grows. Fewer missed orders → more income → couriers stay.

**Data:** Bolt Send rider history and performance files, Jan 2025 – Aug 2026. Main comparison: bicycles May–Aug 2025 (45,947 orders) vs motorbikes May–Aug 2026 (9,086 orders), optional rides excluded.

---

## Opening

**1. Cover: When couriers win, eWAKA grows**
Fewer missed orders → more income → couriers stay.

**2. Couriers miss too many orders**
- **14.0%** of orders get no response (6.9% in 2025)
- Couriers get **KSh 0** for customer no-shows and cancellations
- **13 of 23** new couriers left before August
- Our answer: more couriers online at peak, pay for wasted trips, support new couriers

**3. How an order works**
- Customer orders in the Bolt app; 96% pay cash
- Bolt Send offers each order to a nearby courier
- Courier delivers and hands the cash to Bolt
- eWAKA leases the bikes, trains couriers, pays them weekly

---

## Q1. What drives courier performance?

**4. Motorbikes: 2× faster, but fewer orders finished**
- 21 motorbike couriers vs 21 random bicycle couriers (500 draws, averaged)
- Completed per online hour: **1.50 vs 0.73** (2× faster)
- Completion rate: **56.0% vs 59.6%** (lower)
- Question: if motorbikes are faster, why do more orders fail?
- Note: the 2026 fleet is smaller, so each courier gets more orders.

**5. Missed orders doubled: 7% → 14%**
- What happened to every 100 orders: courier didn't answer **6.9% → 14.0%**, the biggest change of any outcome
- Once a courier says yes, motorbikes finish **more**: 66.8% vs 64.3%
- So orders are lost **before** couriers accept
- (Notes: if no-response had stayed at 2025 levels, completion would be ~61.6%. Slower pickups also see more customer cancels: 23% → 34%.)

**6. Too many orders at once**
- **Orders pile up:** many orders hit one courier in the same hour
- **Orders arrive mid-trip:** couriers already on a trip miss about **1 in 4** (23.4% vs 13.2%)
- Takeaway: more orders at once → more misses
- (Notes: 37.5% of motorbike orders arrive in hours with 4+ orders vs 5.9% for bicycles; 24.3% of those are missed. 7 couriers make 26.5% of misses.)

**7. Each miss costs couriers money**
- No response → acceptance score drops → fewer offers → lower income
- Missing 2–3 orders a day costs a courier about **14% of their income**
- (Notes: typical courier-day KSh 1,860 over 6.3 online hours, KSh 308 per hour; gross, before deductions.)

---

## Segments: who stays and who leaves

**8. New couriers quit fast** (23 joined from April 2026)
- **10 stable:** completion 52%, no-response 14%, KSh 1,538 a day
- **7 onboarding failures:** left within 10 days, completion 0–36%
- **6 lasted weeks, then left:** stayed 17–57 days; 4 of 6 out-earned stayers
- 13 of 23 left; 7 of them in the first 10 days

**9. Couriers who don't recover from suspension leave**
- **14** new couriers got suspended
- **Came back (6) → 5 of 6 stayed**
- **Stayed suspended (8) → 7 of 8 left**
- eWAKA: suspensions are mostly about behaviour
- Takeaway: help suspended couriers come back, and most will stay

---

## Q2. How do we fix it?

**10. Four fixes eWAKA can start now**
| Problem | Fix |
|---|---|
| Couriers don't answer | 1. Teach: answer or go offline |
| Too few couriers at busy times | 2. More couriers 12–6 pm |
| No pay when customers don't show | 3. Pay KSh 100 per no-show |
| New couriers quit fast | 4. Help in the first 2 weeks |

eWAKA can start all four now, without waiting for Bolt. (Bonus idea: same-day settlement, appendix A4.)

**11. Fix 1: Answer it or turn it off**
- **Before the shift — Train:** not answering = saying no
- **During the shift — Nudge:** missed 2 in a row? eWAKA calls
- **After the week — Scorecard:** see the money you lost
- **With Bolt — Ask:** no orders during a trip
- Goal: miss half as many orders (**14% → 7%**)

**12. Fix 2: More couriers at peak**
- Busiest time: **12:00–18:00** (44% of orders)
- Couriers **sign up the day before** for a 12:00–18:00 block
- Model C sizes it: **5–7 couriers at 4 pm**

**13. Fix 3: No-shows cost couriers, so pay them**
- Today: **KSh 0** for any customer no-show (2,311 unpaid motorbike no-shows, May–Aug 2026)
- Each no-show wastes up to **17 minutes** (≈ KSh 87)
- Pay **KSh 100 per verified no-show**, only to couriers who stay online and answer
- Cost: **KSh 19,000** for 4 months, under **2%** of fares (≈ KSh 1M)
- Later, with Bolt: a flat KSh 50–100 customer fee, charged after the courier arrives

**14. Fix 4: Better onboarding for new couriers**
- Day 1: training + mentor · Days 1–7: daily check-in · Day 7: coach if completion < 40% · Day 14: review risk
- Also: recruit strong ex-bicycle couriers, behaviour coaching, exit survey
- Goal: keep new couriers past day 14

**15. Start small: a 4-week pilot**
- **Run (months 1–3, eWAKA):** coaching + scorecard, peak time blocks, no-show pay, onboarding
- **Measure (4 weeks, 3–5 couriers):** missed orders, orders finished and income, couriers who stay
- **Take to Bolt (months 3–6):** flat no-show fee, no orders mid-trip
- **Our ask:** a 4-week pilot with 3–5 couriers (pilot no-show pay ≈ KSh 14,000)

---

## Impact and Q3. How can we predict it?

**16. With our fixes: about 10% more income**
- Our model: if couriers miss half as many orders, orders finished go from **56% to 62%**
- Per courier: **+1 order a day**, **+10% income** (about KSh 182 more a day)

**17. Model A: finds orders we can still save**
- Gives every order a risk score
- The riskiest group holds **~80 missed orders a month**, 3 in 10 of all misses
- Use: call the courier first, or send the order to someone free
- (Notes: 46% of the riskiest 10% are missed, 3× normal. Not all can be saved; saving half adds ~40 orders a month.)

**18. Model B: who to coach this week**
- Predicts which couriers will have a bad week (finish under 50% of orders)
- Biggest red flag: **not answering orders**
- Output: a weekly list of who is at risk, and why

**19. Model C: afternoons need 2–3× more couriers** (Ethan)
- Forecasts orders for every weekday × hour
- Need **74 courier-hours a day**, have **28**
- **5–7 couriers at 4 pm**
- Tells eWAKA how many couriers to book each hour

---

## Conclusion

**20. More bikes work only if couriers answer and stay**
- **Problem:** missed orders doubled (6.9% → 14.0%)
- **Cause:** too few couriers at peak (28 of 74 hours), unpaid wasted trips
- **Solution:** peak time blocks sized by Model C, no-show pay, coaching
- **Our ask:** a 4-week pilot with 3–5 couriers, expected courier income about +10%
- **Still need from eWAKA:** pay deductions, settlement options, how misses count in acceptance

**21. Thank you**

---

## Appendix (backup for Q&A)

**A1. Is it the vehicle?** Bicycle misses rose too, from 2% (Jan 2025) to 28% (Mar 2026); motorbikes stayed at 11–16%. Motorbikes miss only 5.8% in light hours. Misses are a fleet problem, not a vehicle problem.

**A2. Month by month, motorbikes 2026:** August had the lightest load (2.31 orders per online hour), the fewest misses (10.9%) and the best completion (62.5%). A signal, not proof.

**A3. Productivity:** ride duration (−0.50) and pickup duration (−0.42) lower rides per hour; optional rides (+0.25) help a little. Utilisation (+0.73) left out because it measures productivity rather than explaining it. More online hours add rides per day, not per hour.

**A4. Bonus idea, same-day settlement:** today couriers hand over all cash and get paid weekly; proposed: keep their share and get paid daily. Needs Bolt's fleet settings; fallback is a same-day M-Pesa payout of 70–80%.

**A5. Roadmap:** start cheap with eWAKA alone, run the pilot, then negotiate with Bolt.

**A6. Limitations:** different years (checked in A1) · small samples · no order IDs (Model C is an upper bound) · no cancellation timing · income is gross · Bolt's dispatch rules unknown.

---

## Q&A cheat sheet

- **How accurate are the models?** AUC 0.75 (Model A) and 0.93 (Model B), where 1 = perfect and 0.5 = a coin flip, tested on months the models had not seen.
- **Isn't 2025 vs 2026 just a time difference?** Appendix A1: bicycle misses rose too, so it's the fleet, not the vehicle.
- **Can you really save 80 orders a month?** Not all of them. Even saving half adds about 40 orders a month.
- **What does eWAKA gain?** More finished orders and fewer couriers leaving mean more revenue per bike. (We don't have eWAKA's revenue in the data.)
- **How did you sample bicycles?** All 21 motorbike couriers vs 21 bicycle couriers picked at random from 213, repeated 500 times and averaged.

## Where the numbers come from

- BoltSend_eWAKA_analysis.ipynb: slides 2–16 and appendix A1–A3
- BoltSend_eWAKA_prediction_models.ipynb: Models A and B (slides 17–18)
- demand_forecast.py / demand_forecast.csv (Ethan): Model C (slides 12, 19)
- BoltSend_Rider_Allocation_Analysis.ipynb (Ethan): pickup speed vs cancellations
