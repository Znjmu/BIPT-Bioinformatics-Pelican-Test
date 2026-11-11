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