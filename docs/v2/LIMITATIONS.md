# BIPT v2.0: scope and limitations

## What a score means

A score describes one collected WorkBuddy configuration on one frozen synthetic finite-clonal-panel task, evaluated over one released case and two organizer-held cases. It does not measure general biomedical research ability, real experimental validity, clinical performance or the provider's model in every deployment. The biological setting is synthetic; numerical identifiability and decision-theory results are conditional on the supplied model.

The task requires code that transfers between cases and reports case-specific scientific evidence. A correct released-case narrative cannot substitute for a missing or contradictory hidden-case report. Conversely, valid non-unique optimal solutions and tight certificates receive their frozen numerical credit even when accompanying prose is wrong. Numerical, scientific and delivery components are therefore shown separately.

## Difficulty calibration and selection

The benchmark was iteratively hardened during development in response to high earlier scores. Difficulty calibration explicitly aimed to move the DeepSeek Flash development result toward roughly 50/100 by adding substantive scientific requirements. The observed frozen development result was 38.65; scores were not rescaled to reach the target. This development result influenced task selection and is not a newly blinded comparison result.

The subsequent cross-model round froze the participant files, exact prompt, hidden cases, reference answers and grading rules before dispatch. New comparison scores were not used to revise this release's task or rubric. The development baseline is identified with an asterisk in figures and a separate role field in the tables. A cleaner future generalization study would preregister new task instances and evaluate every model prospectively, including a fresh Flash generation.

## Repetition, evaluator and uncertainty

There is one uncontaminated generation per configuration. Replaying its code three times on different supplied cases is not three independent generations, and these heterogeneous cases are not random biological replicates. We report exact observed values without confidence intervals, significance tests or claims of statistically established superiority. Ranking can change with another generation, task instance, reasoning setting or service implementation.

The fixed numerical grader awards 60 points per case and delivery checks award 5. The remaining 35 points require the same Codex evaluator to inspect ten scientific items and their case-specific evidence. Fixed instructions, artifact hashes and item-level published deductions improve auditability, but do not establish inter-rater reliability. The evaluator is not certified to be free of judgment error or provider-related bias. Item evidence can be challenged independently without silently changing the frozen score.

## Practical service budgets

All fresh runs receive a 60-minute external service wall-clock ceiling; predeclared credit ceilings differ by configuration. Actual credits and elapsed time are observed from WorkBuddy. Credits are a service billing unit, not tokens, FLOPs, energy or a stable currency conversion. This design compares practical service outcomes and does not control inference compute. Generation tasks can overlap two at a time; final scoring reruns are serial under the same 360-second per-case ceiling. Local load and unexposed service behavior may still affect runtime.

The exact visible built-in model names are recorded. We do not independently certify the underlying weights, service routing, upstream version or hidden reasoning settings. DeepSeek V4 Pro versus V4.1 Flash and MiniMax M3 versus M3.1 Flash differ in version labels as well as tier. GLM's standard menu label contains no Pro suffix. Within-provider differences are configuration comparisons, not causal estimates of a speed-tier effect.

## Missing and interrupted work

A service-completed submission that fails a subsequent hidden replay receives its actual frozen artifact points, with nonzero exits shown explicitly. Correct partial artifacts can retain points. An external time/credit stop or provider failure is marked incomplete and receives no completed ranking score. An operator-contaminated attempt is excluded and its credit cost is retained as operator overhead, rather than attributed to model ability.

One initial GLM Flash attempt was cancelled after a title-editing focus error sent a task label as a follow-up. Its 0.78 credits are included in comparison overhead. The replacement used a clean directory and the identical original prompt, with no corrective advice. The contaminated attempt is not an independent generation replicate in the scientific comparison.

Five of seven fresh configurations reached their credit stop before normal service completion. The broad intended score comparison and the GLM/MiniMax completed-score pairs therefore remain unresolved. This high interruption fraction limits interpretation of the three available completed scores and indicates that these practical allocations often did not cover the full workflow. It does not establish that the interrupted configurations could not solve the task with different resources.

The service credit display updates in jumps, so a displayed stop is not an exact final bill. Actual settled charges remained within each configuration's allocation. During Step's run, macOS temporarily stopped exposing the task window to accessibility control; a native window image still showed the running task, and control returned after the user reopened the main window. The task was stopped at the first restored reading above its predeclared stop, with a final bill of 252.88 against its 280-credit allocation. No follow-up prompt was sent. This monitoring gap is an operational limitation.

## Reproducibility and disclosure

The repository supplies the released inputs, participant prompt, scoring policy, result tables, review summaries and figure source. Active hidden inputs, truth and grading source remain organizer-held. Public consistency checks verify the published arithmetic and file integrity; they cannot reproduce official hidden-case scores without the protected organizer package.

Separate working directories and explicit access instructions provide workflow isolation, not an operating-system security boundary. We did not certify that a desktop agent could never access other local files. Original submissions and detailed case evidence are archived locally; public summaries omit hidden identifiers and values to limit leakage. Once results and failure categories are public, future blind trials should use fresh undisclosed instances.

## Relationship to v1.0

Version 1.0 concerns synthetic plant-variant prioritization and uses a different automatic rubric and case weighting. Version 2.0 concerns finite clonal panels, identifiability, shared batch states, selection and robust adaptive design, with explicit scientific review. Their numerical scores must not be merged, used as a longitudinal model improvement metric or read as directly comparable difficulty-adjusted measurements. Historical v1.0 materials remain available separately.

All results and interpretations represent the author's views only. They are not provider or institutional certification, endorsement or an official general-purpose model ranking.
