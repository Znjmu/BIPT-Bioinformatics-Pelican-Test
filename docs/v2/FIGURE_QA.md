# Final completed-comparison figure quality checks

Checked 2026-11-18 after all eight configurations reached normal generation completion and all24 case replays were attempted. The dataset contains240 scientific-item decisions. Five resumed original generations are marked +; the development Flash baseline is marked *.

## Data and visual checks

| Figure | Checks |
|---|---|
| score_and_case_comparison | All8 totals decompose into weighted numerical/scientific/delivery components; model order is consistent across panels. All24 unweighted case scores are shown, including failed replays marked !. Partial numeric results retain frozen credit. No unfinished-generation NA remains. |
| paired_and_resource_comparison | All3 provider pairs have3 matched-case differences. Scatter uses all8 actual scores and total initial+continuation bills. Resumed labels and development marker are explicit. Labels, leader lines, axes and legends were inspected. |
| execution_resources | All8 model bills and displayed service durations match source rows; bars separate original and neutral-continuation phases. Original interrupted segments remain in total cost. Calendar idle time and compute equivalence are not inferred. |

Every actual exported PNG was opened and inspected across the complete figure and each panel. Titles, axes, totals, heatmap cells, labels, footnotes and legends fit without clipping or overlapping. All data derive from final original-submission scores and settled observed bills; no synthetic placeholders, confidence intervals or significance tests are drawn.

## Export and font checks

R/ggplot2/grid produces editable-text PDF, editable-text SVG and600-dpi PNG for every figure. Source parsing passed; the source preflight reports18passes,2warnings,0failures. Warnings concern the generic request to run R parsing (performed) and missing TIFF (this GitHub package supplies PDF/SVG/PNG, not a journal TIFF submission).

| Figure | Pages | Extractable text spans | Effective point range |
|---|---:|---:|---|
| execution_resources | 1 | 43 | 7–10 pt |
| paired_and_resource_comparison | 1 | 51 | 7–10 pt |
| score_and_case_comparison | 1 | 71 | 7–10 pt |

The raw PDF text-operator checker was run on all3 PDFs and reports normalized Tf=1, below its simple threshold. Base-R PDF applies the actual scale through the text transformation matrix, so Tf alone is not displayed glyph size. Separate effective-text extraction gives7–10pt in every figure, above the5pt floor. Actual PNGs were also visually checked. The raw-operator result is recorded as an audit-tool limitation, not silently reported as passed.

The public validator confirms all8 completed-generation rows,24 case rows,240 scientific items, phase arithmetic, exact neutral-prompt hash, frozen released inputs and ZIP, figure signatures and editable SVG text. It verifies published consistency, not independent correctness of protected hidden truth or inter-rater reliability.
