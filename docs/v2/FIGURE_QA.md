# Final comparison-figure quality checks

Checked 2026-11-18 after all seven fresh main runs were archived and their bills settled. All three figures use the final eight-configuration table: three completed scores, including the explicitly marked development baseline, and five externally interrupted configurations.

## Data and scientific encoding

| Figure | Panel checks |
|---|---|
| `score_and_case_comparison` | Weighted numerical/scientific/delivery components sum to each completed total within rounding; model order is fixed consistently in both panels. The case matrix uses unweighted case scores. A nonzero replay exit is marked `!`; externally interrupted generations remain grey NA and have no fabricated score. |
| `paired_and_resource_comparison` | Only the finalized DeepSeek pair has three matched-case differences. The missing GLM and MiniMax completed-score pairs are not inferred. The resource scatter contains only three completed scores and explicitly directs readers to the all-outcome cost chart. Labels, provider colors and elapsed times match source rows. |
| `execution_resources` | All eight finalized configurations appear in both credit and elapsed-time panels, including all five external stops. Costs and times match recorded service bills; the historical baseline cost is separate from the new comparison ledger. Completion status uses a distinct grey/blue legend. |

The actual exported PNGs were opened and inspected panel by panel. Model labels, legends, captions, values, axes and footnotes fit without overlapping one another or clipping. All plots state the development-baseline limitation; no error bars, confidence intervals or significance tests are added. Cross-version provider pairs are not represented as controlled speed-tier experiments.

## Export checks

All drawing and rendering uses R (`ggplot2`, base `grid`, `svglite`, `ggrepel`, `ragg`). Each figure has an editable-text PDF, editable-text SVG and 600-dpi PNG. No raster artwork is substituted for the PDF text.

| Figure | PDF pages | Extractable text spans | Effective text sizes |
|---|---:|---:|---|
| execution_resources | 1 | 40 | 7–10 pt |
| paired_and_resource_comparison | 1 | 36 | 7–10 pt |
| score_and_case_comparison | 1 | 71 | 7–10 pt |

The final R source passed parsing and the figure-source preflight returned 18 passes, two warnings and zero failures. The warnings were the generic request to run R parsing, which was done, and the absence of a TIFF submission raster. This GitHub release supplies the requested preview and editable formats; it is not a journal-specific TIFF submission package.

The simple PDF content-stream audit reports a normalized `Tf` value of 1 in base-R PDFs. This alone is not the displayed glyph size: R applies the font scale in the text transformation matrix. A separate effective-text inspection using PyMuPDF extracted 7–10 pt spans in every figure, above the 5 pt floor. The actual rendered images were also checked. The normalized-operator finding is therefore recorded as an audit-tool limitation rather than mislabeled as a passed raw-operator check.

The public release validator checks PNG signatures, PDF signatures, editable SVG text, source-table arithmetic and the public task hashes. These checks verify the published artifacts, not the correctness of protected hidden truth or the reliability of scientific judgment.
