# Fixed evaluator prompt — BIPT v2.0

Evaluate every model's complete archived project using the same frozen BIPT15 organizer package, identical runtime and one fixed evaluator configuration. Do not show this prompt, hidden data, reference answers or prior model submissions to a participant.

1. Verify the participant received the same public package and prompt. Record the original service model label, completion status, elapsed time, actual credits and any operator/provider interruption.
2. Archive the original project and calculate hashes before running it. Do not repair its code or substitute another model's files.
3. Execute its original `bash run.sh INPUT_DIR OUTPUT_DIR` on the released case and both organizer-held cases, with 360 seconds per case. Preserve exit codes, standard output/error and every produced artifact. Apply the frozen numerical and delivery grader.
4. Read every actually delivered R01–R10 section and inspect each actual PNG. Missing hidden reports cannot be replaced by the public report. Award 3.5/1.75/0 under the frozen task rubric, with concrete artifact evidence and a reference/countercheck for each judgment. Assign one scientific error once; do not let a correct table cancel contradictory prose.
5. Review all non-unique solutions by feasibility and achieved objective, not elementwise equality with a reference mixture. Keep automatic scores and scientific-review points separate.
6. Use weights 0.20/0.40/0.40. Report an interval until scientific review is complete. Mark operator-contaminated attempts excluded and externally stopped attempts incomplete; report credit overhead separately. Completed submissions that fail reruns retain their actual frozen artifact score with explicit failure labels.
7. Publish the case-level and component results, deduction reasons, actual costs and limitations. Compare only this frozen version. Never change the rules or suppress a result to reach a target score.

The protected organizer package is required for official hidden-case scores and is not included in this public repository. Use the same evaluator for all submissions; the v2.0 scientific component contains evidence-grounded evaluator judgment and must not be described as entirely automatic.
