# BIPT v2.0 evaluation protocol

This round uses the prospectively frozen BIPT15 finite-clonal-panel task. It is a different scientific and scoring task from v1.0 plant-variant analysis; the two leaderboards must not be merged or interpreted as a common scale.

Every configuration receives the same participant files and byte-identical Chinese prompt in a fresh local WorkBuddy workspace. The hidden cases, reference results, grading program and 0/1.75/3.5 scientific-review rubric remain fixed. The evaluator is the same Codex-primary-common-evaluator throughout. Models receive no hidden data, previous solutions or follow-up corrections. Isolation is by separate directories and explicit access instructions, not an operating-system security boundary.

## Score

- Numerical correctness: 60 per case, computed by the frozen deterministic grader.
- Scientific interpretation: ten evidence-grounded items, 3.5 each. Correct core and required case-specific evidence earns 3.5; correct core missing required evidence earns 1.75; missing content or an explicit scientific error earns 0. The same error is assigned once, and correct tables do not cancel contradictory scientific claims.
- Re-execution/delivery: 5 per case, requiring successful exit and all fourteen valid artifacts.
- Case weights: released 20%, held-out 1 40%, held-out 2 40%.

The 35-point scientific component is reviewed by a fixed evaluator. It is not an entirely deterministic or independently replicated human judgment. Evidence and reasons for deductions accompany the published results. This differs from v1.0's automatic rubric.

Any feasible optimal mixture, physical witness or valid tight vector certificate is accepted; exact copying of an oracle's non-unique solution is unnecessary. A plain notes string is not penalized. All original artifacts are archived before scoring; the evaluator does not repair a submission and then claim the repaired score as the original result.

## Execution and resource accounting

The planned main comparison includes the completed DeepSeek-V4.1-Flash development baseline and seven fresh WorkBuddy configurations. Every new run has a maximum 60-minute service wall-clock allowance and a predeclared credit stopping point. Credit ceilings differ by service configuration and are disclosed with actual consumption. Consequently, this is a comparison under practical service budgets, not a token- or compute-matched experiment. At most two generation tasks overlap; all final grading reruns are serial, in the same local environment, with 360 seconds per case.

The predeclared optional Kimi Pro extension is activated only after all seven main new runs are settled and sufficient authorized credit headroom remains. It is not selected based on observed scores. WorkBuddy's exact visible model labels and fee multipliers are recorded; provider weights, upstream model routing and reasoning settings are not independently certified.

An external budget/time stop, provider failure or operator abort is marked incomplete, not presented as a normal completed ability score. A service-completed submission that subsequently fails a hidden rerun receives the frozen artifact score, with the execution failure stated separately. Operator-contaminated runs are excluded from ranking but their actual credit overhead is accounted for.

## Interpretation boundaries

The Flash development baseline helped calibrate task difficulty before this cross-model comparison. Task selection was therefore not independent of Flash performance. New models see the task only after freezing. A single completion per configuration does not establish statistical model superiority, and three heterogeneous cases are not three random independent biological replicates. Re-executing the same code is a reproducibility check, not an independent generation replicate. No confidence interval or significance test is estimated.

DeepSeek V4 Pro versus V4.1 Flash and MiniMax M3 versus M3.1 Flash also differ in version labels. GLM's standard model has no Pro suffix in the menu. These are within-provider configuration comparisons, not controlled ablations of one speed tier.

The public release contains only released-case inputs, prompts, methods, aggregate results and non-sensitive audit summaries. Hidden inputs, true counts, scoring source and original private workspaces remain organizer-held. Do not give the evaluator prompt or results discussion to participating models during a fresh test.
