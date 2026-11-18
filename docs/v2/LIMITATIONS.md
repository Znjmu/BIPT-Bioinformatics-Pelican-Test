# BIPT v2.0: scope and limitations

## What a score means

A score describes one collected WorkBuddy configuration on one frozen synthetic finite-clonal-panel task, evaluated over one released case and two organizer-held cases. It does not measure general biomedical research ability, real experimental validity, clinical performance or the provider's model in every deployment. The biological setting is synthetic; numerical identifiability and decision-theory results are conditional on the supplied model.

The task requires code that transfers between cases and reports case-specific scientific evidence. A correct released-case narrative cannot substitute for a missing or contradictory hidden-case report. Conversely, valid non-unique optimal solutions and tight certificates receive their frozen numerical credit even when accompanying prose is wrong. Numerical, scientific and delivery components are therefore shown separately.

## Difficulty calibration and selection

The benchmark was iteratively hardened during development in response to high earlier scores. Difficulty calibration explicitly aimed to move the DeepSeek Flash development result toward roughly 50/100 by adding substantive scientific requirements. The observed frozen development result was 38.65; scores were not rescaled to reach the target. This development result influenced task selection and is not a newly blinded comparison result.

The subsequent cross-model round froze the participant files, exact prompt, hidden cases, reference answers and grading rules before dispatch. New comparison scores were not used to revise this release's task or rubric. The development baseline is identified with an asterisk in figures and a separate role field in the tables. A cleaner future generalization study would preregister new task instances and evaluate every model prospectively, including a fresh Flash generation.

## Repetition, evaluator and uncertainty

There is one original generation per configuration; five stopped tasks later receive identical neutral continuation messages in the same chat and directory. These are resumed completions, not new independent generations. Replaying its code three times on different supplied cases is not three independent generations, and these heterogeneous cases are not random biological replicates. We report exact observed values without confidence intervals, significance tests or claims of statistically established superiority. Ranking can change with another generation, task instance, reasoning setting or service implementation.

The fixed numerical grader awards 60 points per case and delivery checks award 5. The remaining 35 points require the same Codex evaluator to inspect ten scientific items and their case-specific evidence. Fixed instructions, artifact hashes and item-level published deductions improve auditability, but do not establish inter-rater reliability. The evaluator is not certified to be free of judgment error or provider-related bias. Item evidence can be challenged independently without silently changing the frozen score.

## Resources and interrupted work

The initial phase used a 60-minute service allowance and different predeclared credit stops. After five tasks were externally interrupted, the user explicitly removed generation stopping limits. The five were resumed without score feedback or scientific corrections, using one common neutral instruction until normal completion. Final tables therefore contain eight service-completed configurations, including the development baseline. Initial capped outcomes remain preserved separately. A resumed result is conditional on its original context, partial code and follow-up message; it is not equivalent to a fresh uninterrupted trial.

Initial and continuation credits and displayed durations are disclosed separately and summed per model. In-progress estimates can reset; only observed final segment bills are settled. Displayed service time is not necessarily all elapsed calendar time. Credits are a billing unit, not tokens, FLOPs, energy or a stable currency. Different resources and interruptions prevent a compute-controlled efficiency claim. At most two generations overlap, and serial grading retains the same 360-second per-case limit. Local load and hidden service behavior may affect runtime.

The exact visible model names are recorded; underlying weights, routing, upstream versions and hidden reasoning settings are not independently certified. DeepSeek and MiniMax pairs differ in version as well as tier. GLM standard has no Pro suffix. These are configuration contrasts, not causal speed-tier effects.

Service completion and successful hidden replay are separate. A normally completed submission can receive low artifact points or fail a hidden entry; correct partial outputs retain their prescribed points. The evaluator does not fix source code. One early GLM Flash attempt received a task-label follow-up after an operator focus error; its0.78credits are overhead and excluded from ability scores. The replacement used a clean directory and identical original task prompt. During the initial Step run, native accessibility control temporarily lost the task window; the historical archive records the monitoring gap and external stop. Later neutral completion is disclosed rather than treating that initial stop as model incapability.

## Reproducibility and disclosure

The repository supplies the released inputs, participant prompt, scoring policy, result tables, review summaries and figure source. Active hidden inputs, truth and grading source remain organizer-held. Public consistency checks verify the published arithmetic and file integrity; they cannot reproduce official hidden-case scores without the protected organizer package.

Separate working directories and explicit access instructions provide workflow isolation, not an operating-system security boundary. We did not certify that a desktop agent could never access other local files. Original submissions and detailed case evidence are archived locally; public summaries omit hidden identifiers and values to limit leakage. Once results and failure categories are public, future blind trials should use fresh undisclosed instances.

## Relationship to v1.0

Version 1.0 concerns synthetic plant-variant prioritization and uses a different automatic rubric and case weighting. Version 2.0 concerns finite clonal panels, identifiability, shared batch states, selection and robust adaptive design, with explicit scientific review. Their numerical scores must not be merged, used as a longitudinal model improvement metric or read as directly comparable difficulty-adjusted measurements. Historical v1.0 materials remain available separately.

All results and interpretations represent the author's views only. They are not provider or institutional certification, endorsement or an official general-purpose model ranking.
