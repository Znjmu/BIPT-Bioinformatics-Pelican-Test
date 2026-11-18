# BIPT v2.0 evaluation protocol

This comparison uses the prospectively frozen BIPT15 finite-clonal-panel task. It differs from v1.0 plant-variant analysis; the two leaderboards are not on a common scale.

Every new configuration initially receives the same participant files and byte-identical Chinese prompt in a fresh local WorkBuddy workspace. The hidden cases, reference results, grader and scientific rubric remain fixed. The same Codex-primary-common-evaluator reviews every submission. Models receive no hidden inputs, previous solutions, score feedback or corrective hints. Separate working directories and explicit access instructions provide workflow isolation, not an operating-system security boundary.

## Frozen score

- Numerical correctness: 60 per case, computed by the frozen grader.
- Scientific interpretation: ten R01–R10 items worth 3.5 each. Correct core and required case evidence earns 3.5; correct core with incomplete required evidence earns 1.75; missing content or an explicit scientific error earns 0. The same specific error is assigned once. Correct tables do not erase contradictory scientific prose.
- Re-execution/delivery: 5 per case, requiring successful exit and all fourteen valid artifacts.
- Case weights: released 20%, held-out 1 40%, held-out 2 40%.

Any feasible optimal mixture, physical witness or valid tight vector certificate is accepted; exact copying of a non-unique reference solution is unnecessary. Original projects are archived before scoring. The evaluator does not repair a submission. All final grading reruns are serial with the same 360-second per-case limit.

## Initial capped phase and completion follow-up

The main comparison comprises seven fresh configurations plus the reused DeepSeek-V4.1-Flash development baseline. The initial phase used predeclared model-specific credit stops and a 60-minute service allowance. Two fresh configurations completed; five were externally stopped before normal completion. That partial report remains preserved in [historical tables](../../results/v2/history_capped/) and [the initial publication](https://github.com/Znjmu/BIPT-Bioinformatics-Pelican-Test/tree/8f6163cccc2858cf8aada39b688e98dacc5f52ce).

The user subsequently removed generation credit/time stopping limits and requested completion of every configuration. The five stopped models were resumed in their original chats and independent directories, using the same [neutral continuation prompt](CONTINUATION_PROMPT.md). The continuation repeats the original access boundary and asks the model to finish; it supplies no scientific correction, result, score or hidden-case information. At most two generation tasks run concurrently. Any further service interruption is recorded, and the identical neutral continuation is used until normal completion. Final evaluation uses the unchanged task and scoring rules.

These five results describe **completion after external interruption**, not fresh independent generations or equal-compute trials. They are marked with a plus sign in tables and plots. Their original stopped archives, continuation dispatches and final original projects are retained by the organizer. [Execution phases](../../results/v2/execution_phases.csv) report initial and continuation credits/time separately; totals sum all observed final bills and displayed service durations. Interim credit estimates may jump or reset and are not summed as final charges. Displayed service time need not include all chat-to-chat idle wall time.

Operator overhead is retained separately from model costs. The initial contaminated GLM Flash attempt remains excluded. The historical optional Kimi extension was not activated in the capped phase; it is outside this completion follow-up's eight-configuration scope. The exact WorkBuddy model labels are recorded; underlying weights, upstream routing and hidden reasoning settings are not independently certified.

A normal service completion can still fail a hidden replay. Such a submission receives its actual frozen artifact score, with execution failures stated explicitly. Completion of the service response is distinct from successful scientific transfer.

## Interpretation and reproducibility

The reused Flash baseline helped select task difficulty and is marked with an asterisk. Task selection was not independent of its performance. There is one original generation per configuration, with disclosed follow-up messages for the five resumed tasks. Re-executing code is a reproducibility check, not another generation replicate; heterogeneous cases are not random biological replicates. No confidence interval, significance test or general model-superiority claim is inferred.

DeepSeek V4 Pro versus V4.1 Flash and MiniMax M3 versus M3.1 Flash also differ in version labels. GLM standard has no Pro suffix in the menu. Provider pairs compare configurations, not a causal speed-tier effect. Credits are observed service bills, not tokens or matched compute.

The 35 scientific points require fixed-evaluator judgment. Published item decisions and artifact hashes support auditability, but do not establish inter-rater reliability. Public validation checks published arithmetic and file integrity; official hidden scoring requires the protected organizer package. Public results reveal task characteristics, so future blind tests should use fresh undisclosed instances. Do not give the evaluator prompt or results discussion to participating models.
