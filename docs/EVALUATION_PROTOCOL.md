# Study protocol: AI-agent evaluation and grader execution

The following is the **historical BIPT v1.0 test design** and the recommended procedure for future experiments. The archived comparison was performed on 11 supplied submission directories; complete agent interaction logs and precise wall-clock times are **not included** in this public release.

## A. Candidate-side protocol

**Distribute only** the original research request and synthetic input files under `benchmark/Leaf_Pigment_Genetics/`. In the historical blind round, the participating agents were not explicitly told that the research request was a competitive AI benchmark.

Example neutral candidate message:

> Please complete the attached plant-genetics research project. Read `PROJECT_REQUEST.md`, `DATA_DICTIONARY.md`, and `RESULT_FORMAT.md`; analyze the provided data, produce the required output files, and deliver reproducible code. Prioritize biological and statistical correctness over formatting. Complete the workflow without intermediate approval requests.

> [!IMPORTANT]
> **Do not mention** the scoring weights, private references, hidden seed values, failure-mode checklist, or benchmark rankings in the candidate prompt. These would directly change the task's difficulty and contaminate the evaluation.

### Mandatory candidate deliverables

Each submitted directory must contain an executable `run.sh` with this interface:

```bash
bash run.sh /path/to/input_data /path/to/output_dir
```

The generated output directory must contain:

```text
variant_consequences.tsv
variant_qc.tsv
accession_gene_burden.tsv
summary.json
segregation.png
interpretation.md
```

Detailed column names are specified in the public `RESULT_FORMAT.md`. The agent may use R and/or Python. All gene/variant/sample identifiers must be read from data rather than copied into source code.

### Controlled model settings

In a formal replication, record the exact agent wrapper, API endpoint, released model identifier, inference effort, context size, computer resource limits, allowed packages, access to the internet, number of retries, and a monotonic start/finish timestamp.

**Predeclared 30-minute ceiling:** Time budget is **1,800 seconds of wall-clock time**. At the deadline, freeze the filesystem and do not accept modified files. If the model returns earlier, record its actual elapsed time. In the historical results published here, per-model timer records were not retained, so this repository does **not** support quantitative claims about model completion speed.

**Hardware/privilege fairness:** Ideally evaluate one model at a time on the same runtime image (or isolate CPU/RAM quotas), with the same environment and identical software dependencies. Simultaneous jobs on one host can create resource contention. Reasoning modes differed in the uploaded runs and were not standardized to equal token or compute budgets.

## B. Organizer-side grading

The private scorer is **not** given to the candidate. It regenerates held-out cases with the same file interfaces and checks the candidate's actual outputs after re-running source code.

**Never use another AI as a subjective judge.** An independent coding agent may orchestrate calls to `grade.py` and format the reports, but the **numeric values must originate from the deterministic Python grader**. The agent must not modify thresholds or credit.

### Private scorer example (only when the retired source is available)

Create the reference environment in the `scoring/` folder from the **optional full-disclosure archive**:

```bash
cd scoring
docker build -t bipt-plant:2026 -f Dockerfile .
```

Run one candidate directory:

```bash
python grade.py \
  --submission /absolute/path/to/submissions/Model_A \
  --public-data /absolute/path/to/benchmark/Leaf_Pigment_Genetics/data \
  --output /absolute/path/to/scores/Model_A.json
```

Batch all candidate directories:

```bash
python grade_many.py \
  --submissions-root /absolute/path/to/submissions \
  --public-data /absolute/path/to/benchmark/Leaf_Pigment_Genetics/data \
  --output-dir /absolute/path/to/scores
```

**Caveat:** `grade_many.py` sorts by directory name by default. Map display names via `results/submission_manifest.csv` and do not infer a model's identity from folder name alone.

### Execution isolation

Each candidate codebase is untrusted shell/Python/R code. Use a sandbox providing:

- `--network none` (no external requests by the candidate).
- Read-only mounts for **candidate source** and **current input data only**.
- Separate writable output volume with no shared result files.
- Non-root identity, disabled privilege escalation, dropped capabilities.
- CPU, memory, process-count, and execution-time limits.
- **No mount for organizer secrets, original held-out truth, or scorer code**.
- **No Docker socket exposure** to the candidate.

The optional archived Dockerfile builds the original scoring runtime. Because dependencies were not completely version-pinned, reproduction should record resolved package versions and image digest. Container isolation reduces but does not eliminate security risk; sensitive execution should use an **ephemeral VM** or a dedicated remote worker.

> [!CAUTION]
> The historical comparison used an independent Linux namespace/mount isolation workflow, as recorded in the scoring report. The public ZIP does **not** include a portable reconstruction of that exact namespace runner. The Docker commands above are the intended portable replay protocol and still require validation on the user's own host.

## C. Verification before publishing scores

A valid evaluation should confirm:

1. **Input identity**: confirm every candidate saw identical released data and task instructions.
2. **Runner contract**: ensure `run.sh` can read an arbitrary input directory and write a new output directory.
3. **No leak**: ensure candidate has no access to hidden labels, prior model output, reference programs, or grading rules during the round.
4. **Reference check**: the trusted reference implementation obtains exactly **100/100** on the historical instances.
5. **Weak baseline check**: a purposely flawed baseline scores well below the full reference (historical internal control approximately **24.33/100**).
6. **Artifact check**: required tables, JSON, notes, and valid images are generated and parsable.
7. **Score integrity**: only the frozen weights and reference source are used; retain raw JSON scores and SHA-256 hashes.
8. **Publication caveats**: clearly mark any incomplete submission and include the author-only-views disclaimer.

## D. Conflicts and regrading

**A change in evaluation policy is a new benchmark version.** Do not silently modify the reference candidate priority criterion or accept novel answer equivalence rules after viewing named submissions. If an ambiguity is discovered, publish a clearly labeled **sensitivity analysis** or a **v1.1 rubric**, and rescore **all** submissions consistently.

**Do not assign subjective bonus credit** to favored models. If a reasonable alternative answer is identified, define an objective rule for accepting it before running a revised comparison.
