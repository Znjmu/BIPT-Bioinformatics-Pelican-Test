# Reproducibility, artifact availability, and disclosure policy

## What this public release makes available

This GitHub-ready public package includes:

- The original synthetic v1.0 research-task documents and the **complete released input dataset**.
- The **11-submission leaderboard** (10 valid, 1 missing deliverable) with reported settings and missing-status flags.
- An aggregate JSON containing per-configuration scores and scoring-source SHA-256 values.
- Publication figures: overall rank and released-versus-hidden scientific scores.
- An automated integrity check for the leaderboard and figures (`scripts/validate_release.py`).
- A figure-generation script (`scripts/plot_results.py`) that redraws the main figures from the published CSV.
- A detailed description of the original rubric, categories, weights, fixed candidate-ranking rule, caps, and limitations.

This is **artifact-level reproducibility**, not by itself a complete rerun of every candidate model's agent session.

## What is intentionally *not* in this public package

1. Original candidate-generated source archives from all 11 model configurations.
2. Organizer's v1.0 hidden seed/truth files and the reference oracle implementation.
3. Access keys for any AI model or service.
4. Agent conversations, exact completion timestamps, and inferential token budgets (not fully preserved).

Without the **original model submissions and hidden scorer files**, a reader can verify the **published leaderboard arithmetic and consistency**, but **cannot independently regenerate each model's full 100-point score** from this public repository alone.

> [!IMPORTANT]
> **Disclosure tradeoff:** Publicly disclosing hidden data, generator seeds, and the oracle improves historical auditability but makes the exact v1.0 instances unsuitable for any subsequent blind model evaluation. The two goals require separate artifact sets.

## Optional completed-benchmark source archive

The companion `BIPT_v1_Full_Reproducibility_ARCHIVE.zip` includes the historical `grade.py`, `grade_many.py`, generator core, reference solution, weak baseline, Dockerfile, and secret for the released instance. The held-out instances are **deterministically regenerated** from the original scorer configuration.

After the author decides v1.0 is **retired**, this archive can be published as a transparent scientific appendix, together with a statement that future blinded evaluations will use new, undisclosed instances.

### Reference-scorer regression

A typical verification procedure, after extracting the full archive, is:

```bash
python -m pip install numpy pandas scipy biopython matplotlib pillow pysam
cd scoring
python self_check.py
```

**Expected:** full reference **100.00/100**, intentionally naive baseline below **50/100**. The historical source reports **24.33/100** for that baseline. This local invocation is for trusted organizer code; do **not** use the `local` runner for untrusted model code.

The full archive is arranged so the `self_check.py` relative public-data path resolves at `../public/Leaf_Pigment_Genetics/data`.

### Replaying an archived candidate

If the author also has a candidate's original source directory, validate its `run.sh` and execute the **Docker-isolated** grader exactly as described in [EVALUATION_PROTOCOL.md](EVALUATION_PROTOCOL.md). Preserve a JSON report for each candidate, then compare it to `results/score_details.json`.

**No original model archive is embedded in the public GitHub folder.** There is no claim that all original model submissions can be redistributed under an open-source license.

## Verify the published leaderboard

Run from the top-level GitHub folder:

```bash
python scripts/validate_release.py
```

This verifies data/manifest consistency, result statuses, ranks, headline statistics, key score totals, and published figure presence without installing scientific Python dependencies.

To redraw charts, install Matplotlib:

```bash
python -m pip install matplotlib
python scripts/plot_results.py
```

Figure regeneration does not change official numeric grades. Main historical figures are included as snapshots.

## Suggested versioning policy

- `v1.0-public`: historical methods/results and public input, with original hidden information withheld.
- `v1.0-disclosed`: optionally release all historical scoring logic and seeds **after declaring the version retired**.
- `v1.1` or `v2.0`: develop a new task family and new hidden seeds, pre-register acceptable answer variants, and require multiple independent evaluation repetitions.

## Integrity

The shipped score-details JSON records the source SHA-256 of `grade.py` and `core.py`. This is an identifier for the historical source files; it is **not** proof that the rubric is biologically indisputable or that all vendor configurations were standardized.
