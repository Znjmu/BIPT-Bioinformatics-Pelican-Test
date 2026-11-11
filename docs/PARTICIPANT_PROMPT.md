# Copy-ready participant task prompt

> [!IMPORTANT]
> **This is a neutral research instruction, not a disclosure of the benchmark or its hidden failure modes.** Give the participant **only** the original task directory `benchmark/Leaf_Pigment_Genetics/` (including its input data and Chinese task documents) and the text below. Do **not** give them the scoring package, this repository's evaluation/answers sections, other participants' submissions, or hidden data.
>
> This file is a **reconstructed, reusable instruction template**, not a verified verbatim transcript of each historical model conversation.

## Prompt to send to the research agent

```text
Please complete the attached plant-genetics research project.

Unpack the attached project files. Read PROJECT_REQUEST.md,
DATA_DICTIONARY.md, and RESULT_FORMAT.md carefully before beginning.

Independently inspect the data and select an appropriate biological
and computational analysis workflow. Follow all deliverable requirements
in the attached documents exactly.

Prioritize scientific validity, correct sequence and genotype
interpretation, and reproducible calculations over visual polish.
Do not invent results or substitute assumptions for measured data.

Use R, Python, or both, as appropriate. Submit the complete source
code plus a portable run.sh that accepts two positional arguments:

    bash run.sh /path/to/input_data /path/to/output_dir

Every input identifier, gene/transcript/variant ID, and sample count
must be read from the supplied data rather than hard-coded.
The command must write all required output files to the designated
output directory and should work on new data of the same format.

Execute the pipeline and check the required tables, JSON, plot, and
interpretation file against RESULT_FORMAT.md before finishing.

Complete the work autonomously without intermediate approval requests.
Deliver the full project directory and a concise findings summary.
```

## Organizer-only administration notes

1. **Use the same exact prompt and original Chinese participant-facing task files for every model.** The files ending in `_EN.md` are translations for international readers; replacing the original historic instructions changes the tested condition.
2. **Start an external 1,800-second wall-clock timer when the task and data are made available.** Freeze submitted files at the deadline; record the actual time, model endpoint, inference effort, dependencies, retries, and host hardware.
3. **Isolate workspaces** and prevent access to other submissions or organizer materials.
4. **Do not disclose** the benchmark purpose, failure-mode list, scoring rubric, expected candidate gene, or hidden instances to the participant during a blind trial.
5. **Historical BIPT v1.0 is publicly documented.** A model that can browse this GitHub repository can discover the problem and answers; new genuinely blind comparisons require new undisclosed instances and preferably a new task.

Further reading: [Evaluation protocol](EVALUATION_PROTOCOL.md) · [Task files](../benchmark/Leaf_Pigment_Genetics/).
