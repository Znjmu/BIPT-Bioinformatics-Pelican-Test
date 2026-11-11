# Copy-ready independent scoring-agent prompt

> [!WARNING]
> **For the organizer's trusted scoring agent only.** Never send this prompt, the private grader, oracle results, or hidden-instance data to a participating research agent. The grader determines numeric scores; the third-party AI must **only orchestrate its execution and report the output**, not assign subjective points.
>
> This is a reusable protocol template. Original BIPT v1.0 has already been published; its fixed instances should not be reused to claim a newly blinded comparison.

## Prompt to send to the independent scoring agent

```text
You are the execution and reporting operator for the completed
BIPT v1.0 bioinformatics analysis round.

You have been given:
(1) the original participant-facing synthetic plant-genetics input data,
(2) a PRIVATE organizer-only scoring package containing grade.py,
    grade_many.py, the frozen reference implementation and hidden data
    generator, and
(3) separately named folders containing each participating model's
    submitted source code and generated outputs.

Task: compute an auditable leaderboard using only the packaged,
unmodified deterministic scoring software.

1. Inspect the package layout and read ORGANIZER_GUIDE.md (if present),
   the scoring program help, and docs/EVALUATION_PROTOCOL.md. Inventory
   the submission folders and identify which include a runnable run.sh.
   Associate display model names with their submission directories
   using the organizer's manifest; do not infer identity from directory
   name alone.

2. Validate the grading environment with the trusted reference
   implementation (expected 100/100 on the historical benchmark)
   before processing participant submissions. Record the exact
   grader source hash and software environment.

3. Execute each untrusted submission ONLY in a secure sandbox
   (prefer a disposable isolated VM, or a Docker container with
   no network, no privilege escalation, bounded CPU/memory/runtime,
   read-only mounts of the current input and source, and one separate
   writable output directory). The participant code must not see the
   grading source, hidden truth, Docker socket, or other submissions.

4. Run the supplied grade.py for each submission, or use grade_many.py
   to process the entire batch. Do not modify the rubric, weights,
   reference answers, hidden datasets, score caps, or tolerances.
   Use the command-line help and the archived evaluation protocol
   for exact paths and options.

5. Preserve every original grading JSON and execution log. Build
   leaderboard.csv sorted by final numeric score (highest first),
   with tied ranks for equal scores. Flag missing or non-runnable
   submissions as INCOMPLETE or N/A in the public presentation while
   retaining the scorer's unmodified raw record.

6. Produce a concise Markdown report including exact model labels,
   reasoning settings (as provided by the organizer), total score,
   category-level points, released-vs-held-out comparison, code
   re-execution status, and major recurring error classes.
   Generate simple figures from the saved CSV/JSON data only.
   Do not invent running times or results that were not logged.

7. Check that every published score matches the preserved grading
   JSON. Report any ambiguous scientific reference rule as a
   limitation rather than silently overriding the scorer.
   If changing the rubric is scientifically necessary, propose a
   NEW version and regrade ALL submissions with explicit disclosure.

8. Include the following statement prominently:
   "All results, rankings, conclusions, and interpretations represent
   only the author's views. This independent evaluation is not an
   official endorsement or certification by any AI provider or
   other organization."

Deliver leaderboard.csv, per-model score JSON, a Markdown report,
comparison figures, a provenance/manifest file, and verification logs.
Do not publish the organizer-only scoring package or hidden answers.
```

## Example organizer commands

Run from the private scoring directory with the original task data and the submission directories available. Build the scoring image in advance:

```bash
docker build -t bipt-plant:2026 -f Dockerfile .

python grade_many.py \
  --submissions-root /absolute/path/to/submissions \
  --public-data /absolute/path/to/benchmark/Leaf_Pigment_Genetics/data \
  --output-dir /absolute/path/to/scores
```

> [!CAUTION]
> The public repository **does not contain the private grader**. The organizer must supply the original private scoring package separately. A third-party AI without file execution, sandboxing, and that package **cannot calculate the historical 100-point rubric from scratch**. Never trust its guessed scores.

## Transparency and comparability

- **Freeze the rubric** before examining named submissions.
- Preserve the historical **25% released / 37.5% held-out 1 / 37.5% held-out 2 scientific score**, plus execution/artifact points, as encoded in the private grader.
- Preserve raw scorer output even when publication uses `N/A` for an incomplete submission.
- Distinguish rubric adherence from universally correct biology: alternative gene-prioritization choices may be scientifically defensible.
- **Do not claim a completed blind test** using publicly disclosed v1.0 data as if it were a new hidden evaluation.

Related documents: [Scoring methodology](SCORING.md) · [Evaluation protocol](EVALUATION_PROTOCOL.md) · [Limitations](LIMITATIONS.md).
