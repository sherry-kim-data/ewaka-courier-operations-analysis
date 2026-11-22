# Original competition submission (Team 7)

This folder keeps Team 7's entry to the Santa Clara University MSBA Analytics Showdown (Fall 2026), as submitted before judging. **The revised analysis is in the main folder of this repository.**

**Team 7:** Sinhye (Sherry) Kim · Yan Wu · Wei-Chia Lin (Vivien) · Ethan Casey
**Case partner:** eWAKA (Bolt Send courier fleet, Nairobi)

## Known issues, corrected in the revised version

The judges' questions found these problems. They are left unchanged here as a record of the original work:

- **Slide 6, order load:** counted missed offers as busy time. Counting only answered offers, busyness explains about 3 of the 7.1-point rise in no-response.
- **Slide 6, mid-trip offers:** the mid-trip flag reset after any unfinished order, so mid-trip misses show as 13.7%; corrected, they are 25.5%.
- **Slides 12, 19, 20, "28 of 74 courier-hours":** Model C divided all offers (including optional rides) by a finished-order capacity. The fair comparison is 37 needed vs 28 online.
- **Slide 9, suspensions and exits:** based on each courier's last recorded status, so it can't show that suspensions cause exits. Withdrawn.

## Contents

```
slides/BoltSend_eWAKA_courier_performance.pdf    21 slides + appendix A1–A6 (also .pptx, with speaker notes)
team_notes.md                                    written overview of every slide
code/BoltSend_eWAKA_analysis.ipynb               numbers behind slides 2–16 and appendix A1–A3
code/BoltSend_eWAKA_prediction_models.ipynb      Model A (missed-offer risk) and Model B (next-week low performer)
code/BoltSend_eWAKA_presentation_demo.ipynb      short notebook shown during the talk
code/demand_forecast.py, demand_forecast.csv     Model C: orders and couriers needed by weekday × hour (Ethan Casey)
code/BoltSend_Rider_Allocation_Analysis.ipynb    rider tiers, allocation simulation, pickup speed vs cancellations (Ethan Casey)
```

Courier IDs shown in the original outputs have been replaced with anonymous labels (Courier 01, Courier 02, …).

## Re-running

The eWAKA data files are not included. To re-run, put `boltsend_rider_history.xlsx` and `boltsend_rider_perfomance.xlsx` (original "perfomance" spelling) in the `code/` folder next to the notebooks. Results are saved in each notebook, so they can be read without running.

Packages: pandas, numpy, openpyxl, scikit-learn, matplotlib, scipy, seaborn.
