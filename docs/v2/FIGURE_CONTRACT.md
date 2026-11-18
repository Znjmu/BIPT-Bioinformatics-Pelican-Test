# Comparison figure contract

Core question: where do the observed single-run WorkBuddy configurations differ in frozen-task correctness, scientific reporting, hidden-case transfer and resource use?

Archetype: quantitative grid with a dominant score-decomposition panel. No winner is assumed before scoring.

Backend: R/ggplot2 plus base grid, editable base-R PDF, svglite SVG and ragg 600-dpi PNG. A working Cairo PDF device is an optional export route. White background, stable provider colors, explicit incomplete/excluded symbols. Planned final size about 183 mm wide; text floor 5 pt, direct model labels, source CSV and figure-generation script supplied.

Panel map: (a) total score decomposed into 60 numerical, 35 scientific and 5 delivery points; (b) released/held-out case scores with exit/delivery labels; (c) within-provider configuration differences using the same cases; (d) observed credits versus total score with elapsed time labels; (e–f) actual credits and elapsed minutes for all finalized service outcomes, including external stops. Panels are split across three figures for readability. Resource costs of incomplete configurations are never omitted from the all-outcome resource chart.

Replicate unit: one independent generation attempt per listed configuration. The Flash row is a development/calibration baseline; mark it distinctly. The three cases are fixed heterogeneous scenarios, not random replicates. No statistical test, error bar or confidence interval; repeat execution is not independent generation. No synthetic placeholder observations.

Integrity: every plotted value comes from finalized original-submission scores and actual service bills. Incomplete runs remain visible with status but are excluded from completed-score ordering. Operator aborts are documented in accounting, not ranked as zero ability. Keep v1.0 figures/data unchanged and separate.
