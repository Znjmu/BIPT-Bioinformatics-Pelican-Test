# Quick Start — Beginner's Guide to BIPT v1.0

**No bioinformatics expertise required to follow these instructions.** You can give the research task to an AI coding agent and let it produce the required scripts and results. To assign an **official 100-point BIPT v1.0 score**, however, the organizer must also have the **separate private scoring package** and an isolated environment capable of running it. **The GitHub public repository alone cannot generate an official hidden-data score.**

> [!IMPORTANT]
> **ONE EVALUATOR FOR ALL SUBMISSIONS.** For the fairest comparison, submit **every evaluated model's finished project to the same independent evaluation model** (same model/version, reasoning settings, system instructions and evaluation prompt). Give this evaluator the same deterministic scoring software, environment and rubric for every submission. **The evaluation AI organizes and runs the tests; it must NOT invent or subjectively assign the numeric grades.** The frozen Python grader is the sole source of scores.

## ① Download the task files

1. Open the **[BIPT GitHub repository](../README.md)**.
2. Click GitHub's green **Code** button, then **Download ZIP**.
3. Unzip the downloaded repository.
4. Inside it, open the folder: **`benchmark/Leaf_Pigment_Genetics/`**.
5. Check that it contains `PROJECT_REQUEST.md`, `DATA_DICTIONARY.md`, `RESULT_FORMAT.md` and `data/`.

> [!CAUTION]
> **Do not upload the entire downloaded GitHub repository to a participant AI.** It contains the public leaderboard, evaluation methodology, prompt B and explanations of the historical traps. Give a participant **only** `benchmark/Leaf_Pigment_Genetics/` and **Prompt A**. Otherwise the participant may see the solution context.
>
> BIPT v1.0 is already public. A truly fresh, uncompromised blind test requires a **new undisclosed task and hidden instances**, not simply reusing the public v1.0 files.

## ② Send the task to an AI Agent

1. Choose the AI agent you want to test (for example, an agent that can read files and execute R or Python).
2. Upload **only** the `Leaf_Pigment_Genetics` task folder, or a ZIP containing **only that folder**.
3. Open **[📋 Prompt A — Participant Research Task](PARTICIPANT_PROMPT.md)**. Copy its prompt text into the agent's chat.
4. Give each participating model the **identical task files, exact prompt, computer environment, allowed tools and 30-minute external time limit**. Record the model version and reasoning mode.
5. Let it work independently. Do not give hints about the answer, the hidden traps or the benchmark scoring.

**The agent should think it is completing a normal plant-genetics research project:** identify the most plausible locus behind a pale-leaf phenotype using genomic sequences, gene models, variants, and phenotype observations.

## ③ Collect the agent's complete project

Ask the participant to return **one complete folder** that includes the reproducible analysis source code and `run.sh`, as well as the required outputs. Check that the output directory has all six files:

```text
variant_consequences.tsv
variant_qc.tsv
accession_gene_burden.tsv
summary.json
segregation.png
interpretation.md
```

Keep each model's work **separate** (e.g., `submissions/Model_A/`, `submissions/Model_B/`) and record which folder corresponds to which model. Do not alter its submitted code after the deadline.

> [!TIP]
> If the agent can only provide a ZIP, save the ZIP as-is as your archival submission. Unzip a working copy for scoring. Keep the original archive to verify that no files were changed.

## ④ Give **all** submissions to **one** independent evaluator

1. Choose **one fixed evaluation AI** for the entire batch (for example, one chosen Codex model, fixed to the **same version and reasoning setting** throughout).
2. Provide it with **all** the submissions from Step ③, the original public input dataset, and the organizer's **private scoring package** (kept separate from participants).
3. Open **[📊 Prompt B — Independent Scoring Agent](GRADING_AGENT_PROMPT.md)**. Copy the full prompt to the evaluation AI.
4. Have the evaluator run the **unmodified deterministic grader** against every submission using the **same runtime**, **same hidden test instances**, and **same weights**. Execute submitted code in an isolated container or disposable VM; do not run untrusted `run.sh` directly on your personal computer.
5. Preserve the raw scorer-generated JSON and logs. The evaluator can tabulate results, create plots and explain errors, but **cannot replace the grader with its own subjective scores**.

> [!WARNING]
> **The private `grade.py` and `grade_many.py` are intentionally absent from this public repository.** If you only have the public GitHub files, you can practice the task and inspect the published historical scores, but you **cannot independently issue a verified 100-point result with the hidden tests**. Contact the organizer for authorized access to a scoring environment, or use the separately disclosed full archive only if the benchmark is retired.

## ⑤ Read the score and compare models

1. Read the independent evaluator's `leaderboard.csv` and original per-model grading JSON.
2. Use the scores calculated by the grader, **not** a free-form AI opinion.
3. Check which parts were lost: variant effect annotation, reference/QC, phased alleles, gene prioritization, or evidence interpretation.
4. Include every participant, flagging missing or unusable submissions **N/A / incomplete** in the presentation rather than implying measured zero scientific competence.
5. Publish the method, model settings, software environment, raw grading output, limitations and the author's-views statement.

For historical BIPT v1.0 scores, see the [11-model leaderboard](../results/leaderboard.csv) and [analysis](RESULTS.md).

---

## Five-minute checklist (before sharing any results)

- [ ] Every participant received **the same** task and Prompt A, without access to the scorer.
- [ ] Every participant was given the same external deadline and comparable resources.
- [ ] All submitted projects were frozen and archived without modification.
- [ ] **The same independent evaluation AI/model version/configuration** handled every submission.
- [ ] Numeric marks were produced **only** by the identical frozen deterministic Python grader, with the same held-out inputs.
- [ ] All participant code ran in a restricted isolated environment.
- [ ] The leaderboard agrees with the raw JSON scores and correctly marks incomplete entries.
- [ ] The author-only-views statement is included.

> [!NOTE]
> **Author's views:** All BIPT rankings, conclusions and interpretations reflect **only the author's views**; they are not endorsed by any AI provider, university, or third party. Special thanks to [BioMamba Bioinformatics Base](https://biomamba.top/index.html) for its educational contributions; this acknowledgment does not imply participation or endorsement.

### Useful links

**[📋 Prompt A — Send a task to the participating AI](PARTICIPANT_PROMPT.md)** · **[📊 Prompt B — Evaluate all completed tasks](GRADING_AGENT_PROMPT.md)** · **[Full methodology](EVALUATION_PROTOCOL.md)** · **[Scoring rules](SCORING.md)** · **[Return to README](../README.md)**
