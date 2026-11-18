# The finite-panel task and frozen scoring rules

The participant receives exact synthetic technical-readout expectations for a finite panel of distinct clonal members. Each member has five fixed binary potential responses. Unknown nonnegative integer type counts must satisfy layer sizes, support assumptions and three kinds of jointly conditioned observations. The scientific goal is to identify what these observations determine and design a valid adaptive rescue experiment under worst-case risk constraints.

The inputs and the complete original Chinese mathematical definitions are in [the participant task](../../benchmark/Finite_Panel_Rescue/PROJECT_REQUEST.md). The following is an explanatory guide; it does not replace those definitions or add new grading requirements.

## Why the task is difficult

| Decision | Required distinction |
|---|---|
| Finite population | Integer type counts and without-replacement sampling differ from an arbitrary continuous distribution or independent replacement sampling. |
| Same-member and distinct-member reads | Two clonal aliquots share a biological response; two different members have a different sampling law and conditioning denominator. |
| Shared technical batch | One unobserved batch persists for the whole experiment. Integrate the joint path under that batch; multiplying separately averaged channels generally changes the experiment. |
| Selection enrichment | Successful entry changes both type and batch distributions. Pool the joint numerators and denominators before taking a ratio. Do not transfer cohort-enriched weights to the unscreened target experiment. |
| Partial identification | Point identification, a nontrivial range and an undefined ratio are distinct. A denominator that can be zero but can also be positive does not make the entire query undefined. |
| Outer relaxation | The comparison relaxes both the integer grid and the finite-count quadratic pair relation while retaining all observation constraints through a symmetric pair coupling. Its bounds need not have physical integer witnesses. |
| Protocol legality | Every structural path obeys depth, repeated-action and path-cost restrictions, including missing-read branches. A low-probability or costly branch cannot be excused using average cost. |
| Randomized robust design | One common mixture is used across layers. Nature can know that mixture but must choose a single complete physical panel before protocol identity, members and reads are realized. |
| Two kinds of risk | An experiment-level event probability differs from the expected number of injured members. Conditional member risk is a ratio of pooled expected counts, with explicit empty-exposure handling. |
| Proof of optimality | A physical witness proves attainability. A valid vector certificate across all legal protocols proves the upper bound. Neither an arbitrary loose bound nor an averaged nonphysical panel proves exact optimality. |
| Scientific reporting | Tables, prose, summaries and actual plots must describe the same case, units, thresholds and uncertainty status. Correct code output does not make a contradictory narrative scientifically correct. |

## Score arithmetic

Each case has 60 numerical points, 35 scientific points and 5 delivery points. The final score is:

`0.20 × released_case + 0.40 × held_out_1 + 0.40 × held_out_2`

The numerical categories are query bounds (10), protocol metrics (8), legality audit (4), optimal mixtures (6), mixture metrics (6), protocol conditional safety (4), mixture conditional safety (4), integer witnesses (6), global certificates (8) and summary consistency (4). The fixed grader checks complete correct rows and verifies submitted mixtures against their own probabilities. Non-unique valid optimal solutions are accepted.

Delivery earns 5 only when the original entry point exits successfully and produces all fourteen nonempty valid artifacts, including the required PNG dimensions. A failed replay is stated explicitly; any independently correct partial numerical artifacts retain the credit specified by the frozen grader.

## Scientific review: ten items, 3.5 points each

| Item | Evidence being reviewed |
|---|---|
| R01 | Complete integer-panel enumeration, normalization, support and all three joint observation families; actual sizes, counts and residuals; technical expectations and assumption boundaries. |
| R02 | Identification states, denominators, attainable values and the correctly defined continuous outer relaxation, with actual case comparisons. |
| R03 | Same-slot biological confirmation, event probabilities versus expected member counts, and conditional independence under one persistent batch, with actual joint-read evidence. |
| R04 | Distinct sampling and selection denominators, actual ordered cohorts, envelopes and probabilities, and pre/post-selection batch distributions. |
| R05 | Complete structural-path legality, all illegal identifiers and reasons, depth and cost evidence. |
| R06 | A common mixture and a common adversarial physical panel; protocol-aware comparison, separate certificate mixtures and the random-batch boundary. |
| R07 | All tied pure optima, both optimal mixtures and their support, overall event risk and layer-specific pooled member risk, including undefined exposure and STOP behavior. |
| R08 | Joint utility versus the separate-extrema lower bound, actual cost variation, and the same submitted mixture under the batch-reset diagnostic. |
| R09 | Actual physical witnesses and a valid tight global vector certificate, including multipliers, achieved bounds, feasibility violations and optimality gaps. |
| R10 | Scientific agreement between the actual PNG, summary, prose and tables, including units, thresholds, parameters and states. Errors already assigned to R01–R09 are not counted again here. |

For each item, 3.5 means the core is correct and the required case-specific evidence is supplied; 1.75 means the core is correct but required evidence is incomplete; 0 means missing content or an explicit scientific error, incorrect general formula or contradictory assertion. The same scientific error is assigned once. Separate false claims are reviewed under their corresponding items. A correct table does not erase an explicit opposite claim in prose.

Every model is reviewed by the same evaluator under the same frozen rules. Until that review is complete, the automatic score supports a range rather than a final total. Difficulty targets do not authorize retrospective score changes.

## Public and protected material

The public [participant ZIP](../../releases/BIPT_v2.0_participant.zip) contains only released inputs and the participant prompt. The organizer retains hidden cases, reference answers and grading software. The [published-data validator](../../scripts/validate_v2_release.py) checks released artifacts and reported arithmetic; it cannot reconstruct hidden truth from the public repository. See the [execution protocol](EVALUATION_PROTOCOL.md) and [limitations](LIMITATIONS.md).
