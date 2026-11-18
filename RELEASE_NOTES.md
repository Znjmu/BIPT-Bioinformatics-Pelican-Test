# BIPT v2.0 — Frozen finite-panel comparison

Version 2.0 introduces a synthetic finite-clonal-panel task that combines integer identification, selection-conditioned observations, one persistent shared technical batch and robust adaptive rescue design. It addresses the ceiling effect of the earlier task through new scientific requirements and a new scoring scale. Version 1.0 results remain historical and cannot be directly compared with v2.0 scores.

## Included in v2.0

- A participant-only ZIP, the exact Chinese task prompt, original public inputs and fourteen-artifact output contract.
- Prominent participant/evaluator links and a Chinese/English five-step beginner guide.
- Real WorkBuddy runs in independent directories, using the same frozen task and one fixed evaluator.
- Within-provider standard/Pro and Flash comparisons where those configurations are offered, plus other built-in configurations. All eight configurations now have final completed scores, including five resumed original tasks.
- Separate numerical (60), scientific (35) and delivery (5) components; released/held-out case weights of 20%/40%/40%.
- Evidence-grounded scientific deductions across ten frozen items. Explicit scientific errors receive zero for the relevant item; the same error is not deducted twice.
- Actual initial/continuation credits and displayed service time, historical limits, operator-overhead disclosure and archive/freeze provenance.
- Component/case comparison figures and within-provider/resource figures, with R source and PDF/SVG/600-dpi PNG exports.
- Public consistency checks in GitHub Actions, while active hidden inputs, truth and grading implementation remain protected.

The initial capped comparison is preserved separately. After the user removed generation stops, GLM standard/Flash, MiniMax standard/Flash and Step Preview were resumed in their original chats with a common neutral instruction and no scientific feedback. The same task, rubric and replay limit remain frozen. These are resumed completions, not new independent repeats.

The [results and interpretation](docs/v2/RESULTS.md) provide actual totals, per-case exits, pair differences and scientific-review findings. The [limitations](docs/v2/LIMITATIONS.md) explain difficulty-selection bias, the development Flash baseline, single generations, non-matched compute budgets, version differences and evaluator judgment. No score rescaling, significance test or general model-superiority inference is used.

The historical v1.0 README and hash manifest are preserved as `README_v1.0.md` and `SHA256SUMS_v1.0.txt`. Other original task, result and plotting materials remain in their existing paths.

---

# BIPT v1.0 — Public methodology and results release

**Release scope:** synthetic plant-genetics task, documentation, raw released dataset,
reported leaderboard for eleven submitted AI configurations, detailed scored
results, charts, and verifiable artifact-integrity scripts.

## Highlights

- An independent, fixed **100-point** computer-executed bioinformatics rubric.
- Biological stressors spanning **VCF, FASTA, GFF3, negative-strand CDS,
  transcript-specific effects, allele phase, quality control, and genotype
  segregation**.
- **11 submitted model configurations; 10 valid runnable analyses.**
- Highest observed scores (historical rubric): **DeepSeek V4 Pro 99.62**,
  **GPT-6 Luna (Codex Max) 97.56**.
- Five configurations tied at **93.25**. The valid-submission score mean was
  **93.51**, and **8/10** diverged from the oracle's preferred candidate on
  one held-out instance.
- Full methodological caveat: the oracle's candidate-priority rule is
  **not the only defensible biological interpretation** of the competing
  evidence. A high score is *not* proof of across-domain model superiority.

## Reuse

Download the repository and read `README.md` plus `docs/EVALUATION_PROTOCOL.md`.
This public version intentionally omits historical hidden truth and grader
sources. A separate, **optional full-disclosure archive** is available for
retrospective audit, **only after retiring the exact v1.0 instances from future
blind use**.

> [!IMPORTANT]
> **The results and interpretations presented here represent the author's
> views only.** The repository is independent of, and is not endorsed by,
> any listed AI model provider or other institution.

## Acknowledgments

**Special thanks to BioMamba Bioinformatics Base (Biomamba 生信基地)** for bioinformatics education and open knowledge-sharing. This acknowledgment does **not** imply participation in or endorsement of the benchmark. See [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md).
