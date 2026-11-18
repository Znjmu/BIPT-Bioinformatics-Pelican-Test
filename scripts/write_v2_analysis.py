#!/usr/bin/env python3
"""Describe finalized published observations without inferring population superiority."""
from pathlib import Path
import csv, json

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / 'results/v2'
def read(name):
    with (R / name).open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))
def fnum(row, key):
    return float(row[key])
def main():
    rows = read('leaderboard.csv')
    details = json.loads((R / 'score_details.json').read_text())
    completed = sorted((r for r in rows if r['status'] == 'completed_scored'), key=lambda r: -fnum(r, 'total'))
    incomplete = [r for r in rows if r['status'] != 'completed_scored']
    assert len(rows) == 8 and len(completed) == 8 and not incomplete, 'Completion release requires all eight final scores'
    phases = read('execution_phases.csv')
    cases = read('case_scores.csv')
    reviews = read('scientific_review.csv')
    lines = [
        '# BIPT v2.0 — observed results and interpretation', '',
        f'All {len(rows)} configurations have reached normal service completion and have final frozen scores. Five initially stopped tasks were resumed with the same neutral continuation instruction; these are marked with a plus sign. They are completions of the original generations, not independent new trials. The DeepSeek Flash development baseline is reused and marked with an asterisk.', '',
        '**These are exact single-run observations on a selected synthetic task, not a statistically established general model ranking.** Version 1.0 scores use a different task and scale and are excluded.', '',
        '## Scores and case transfer', '',
        '| Configuration | Total / 100 | Numerical / 60 | Scientific / 35 | Delivery / 5 | Released | Held-out 1 | Held-out 2 |',
        '|---|---:|---:|---:|---:|---:|---:|---:|'
    ]
    for r in completed:
        name = r['model'] + (' *' if r['role'] == 'development_calibration_baseline' else ' +' if r['role'] == 'completion_after_external_interruption' else '')
        values = [f'{fnum(r,k):.2f}' for k in ['total','numerical','scientific','delivery','public_total','hidden1_total','hidden2_total']]
        lines.append('| '+name+' | '+' | '.join(values)+' |')
    for r in incomplete:
        lines.append(f"| {r['model']} ({r['status']}) | NA | NA | NA | NA | NA | NA | NA |")
    lines += ['', 'Case totals are unweighted 100-point case scores; component columns are weighted across cases. The final total uses 20% released and 40% for each held-out case. Every generation is service-completed. A subsequent hidden replay can still fail and receive its actual frozen artifact points; entry failures are shown separately.', '',
              '![Component scores and case outcomes](../../figures/v2/score_and_case_comparison.png)', '']
    lines += ['**Completion follow-up:** GLM standard/Flash, MiniMax standard/Flash and Step Preview were resumed after the user removed generation credit/time stops. Original chats, partial projects and model labels were preserved. No hidden feedback or scientific corrections were supplied. [Initial capped results](HISTORICAL_CAPPED_RESULTS.md) and [phase accounting](../../results/v2/execution_phases.csv) preserve that history. All three planned provider pairs now have final scores.', '']
    if completed:
        best = completed[0]
        lines += [f"The highest observed completed total is {fnum(best,'total'):.2f} for {best['model']}. This is conditional on this task, this submission and this rubric. Numerical correctness, scientific explanation and execution are separate outcomes; the component table is required to understand the total.", '']
    bymodel = {r['model']: r for r in completed}
    if 'Xiaomi MiMo-V2.6-Pro' in bymodel and 'DeepSeek-V4-Pro' in bymodel:
        aa, bb = bymodel['Xiaomi MiMo-V2.6-Pro'], bymodel['DeepSeek-V4-Pro']
        lines += [f"MiMo Pro exceeds DeepSeek Pro by {fnum(aa,'total')-fnum(bb,'total'):.2f} observed weighted points. Its released-case score is lower, but its original entry completes both hidden cases, whereas DeepSeek Pro fails one. MiMo's core protocol metrics and optimal mixtures transfer correctly across all three cases; its copied outer bounds and invalid or incomplete global certificates lose numerical points, while released-case prose reused in hidden reports loses scientific points. Completion and numerical transfer explain the difference more clearly than a broad claim about reasoning quality.", '']
    lines += ['## Within-provider configuration comparisons', '', '| Provider | Standard/Pro | Flash | Total difference (points) | Released difference | Held-out 1 difference | Held-out 2 difference |', '|---|---|---|---:|---:|---:|---:|']
    pairs = [('DeepSeek','DeepSeek-V4-Pro','DeepSeek-V4.1-Flash'), ('GLM','GLM-5.3','GLM-5.3-Flash'), ('MiniMax','MiniMax-M3','MiniMax-M3.1-Flash')]
    pair_details = []
    for family, a, b in pairs:
        aa = next((r for r in completed if r['model'] == a), None)
        bb = next((r for r in completed if r['model'] == b), None)
        if aa and bb:
            vals = [f'{fnum(aa,k)-fnum(bb,k):+.2f}' for k in ['total','public_total','hidden1_total','hidden2_total']]
            lines.append('| '+family+' | '+a+' | '+b+' | '+' | '.join(vals)+' |')
            pieces = [f'{fnum(aa,k)-fnum(bb,k):+.2f}' for k in ['numerical','scientific','delivery']]
            pair_details.append(f"**{family} component decomposition:** the {vals[0]} total-point difference comprises {pieces[0]} numerical, {pieces[1]} scientific and {pieces[2]} delivery points. These are weighted components of this particular pair, not an estimated population effect.")
        else:
            lines.append(f'| {family} | {a} | {b} | NA | NA | NA | NA |')
    lines += [''] + [text+'\n' for text in pair_details]
    lines += ['Differences compare the same three fixed cases. They do not isolate a causal speed-tier effect: DeepSeek and MiniMax labels also differ in version, GLM standard has no Pro suffix, initial budgets and continuation histories differ, and the DeepSeek Flash result helped select task difficulty. No significance test or confidence interval is attached.', '',
              '![Matched-case differences and actual resource observations](../../figures/v2/paired_and_resource_comparison.png)', '',
              '## Execution and resource observations', '', '![Total observed service costs across initial and continuation phases](../../figures/v2/execution_resources.png)', '', '| Configuration | Status | Credits | Service minutes | Successful case exits |', '|---|---|---:|---:|---:|']
    for r in rows:
        successes = sum(int(x['returncode']) == 0 for x in cases if x['configuration_id'] == r['configuration_id'])
        exits = f'{successes}/3' if r['status'] == 'completed_scored' else 'NA'
        lines.append(f"| {r['model']} | {r['status']} | {fnum(r,'credits'):.2f} | {fnum(r,'elapsed_seconds')/60:.1f} | {exits} |")
    lines += ['', f"Initial new comparison runs plus operator overhead consumed {details['original_capped_phase_credits']:.2f} credits; the completion follow-up consumed {details['completion_phase_credits']:.2f}; combined comparison cost is {details['new_comparison_credits_settled']:.2f}. The reused Flash baseline's 38.28 credits belong to development and are outside that total. Operator overhead is {details['operator_overhead_credits']:.2f} and excluded from model scores.", '',
              'The user removed generation credit/time stops before the completion follow-up. No task was terminated to preserve the old allowance. These totals are observed bills, not an account balance or compute-matched budget. The optional Kimi run is outside this eight-configuration follow-up.', '',
              '| Configuration | Initial credits | Continuation credits | Total credits | Initial service min | Continuation service min | Neutral messages |',
              '|---|---:|---:|---:|---:|---:|---:|']
    for ph in phases:
        lines.append(f"| {ph['model']} | {float(ph['initial_credits']):.2f} | {float(ph['continuation_credits']):.2f} | {float(ph['total_credits']):.2f} | {float(ph['initial_elapsed_seconds'])/60:.1f} | {float(ph['continuation_elapsed_seconds'])/60:.1f} | {ph['neutral_continuation_messages']} |")
    lines += ['', 'Only final segment bills are summed. Displayed service time can reset after a continuation and does not necessarily include all calendar waiting time. Both GLM configurations required a second identical neutral continuation after a cancelled segment; those segments are retained in cost accounting. No scientific feedback accompanied those messages.', '',
              'At most two generation tasks overlap. Final scoring reruns remain serial with 360 seconds per case. [The original capped plan](../../results/v2/history_capped/comparison_plan.csv), [completion protocol](EVALUATION_PROTOCOL.md) and [phase table](../../results/v2/execution_phases.csv) distinguish generation resources from the unchanged evaluation rules.', '',
              '## Scientific-error audit', '',
              'The following summaries come from the fixed evaluator\'s case-specific item decisions. They distinguish missing reports, incomplete required evidence and explicit scientific contradictions. They do not imply a recurring error rate for the underlying model.', '']
    for r in completed:
        rid = r['configuration_id']
        lines += [f"### {r['model']}" + (' — development baseline' if r['role'] == 'development_calibration_baseline' else ''), '']
        for case in ['public','hidden1','hidden2']:
            cr = next(x for x in cases if x['configuration_id'] == rid and x['case'] == case)
            items = [x for x in reviews if x['configuration_id'] == rid and x['case'] == case]
            notes = []
            for x in items:
                if float(x['points']) < 3.5 and x['public_note'] not in notes:
                    notes.append(x['public_note'])
            label = {'public':'Released','hidden1':'Held-out 1','hidden2':'Held-out 2'}[case]
            lines.append(f"- **{label}:** numerical {float(cr['numerical']):g}/60, scientific {float(cr['scientific']):g}/35, delivery {float(cr['delivery']):g}/5; entry exit {cr['returncode']}. " + (' '.join(notes) if notes else 'All scientific items were accepted with the required evidence.'))
        lines += ['']
    lines += ['The [item-level review table](../../results/v2/scientific_review.csv) records all R01–R10 points. Missing hidden reports are not replaced by released-case prose. A correct non-unique mixture or certificate retains numerical credit; the same underlying scientific error is not deducted again under R10.', '',
              '## Reading the outcome responsibly', '',
              'The task separates successful numerical optimization from faithful scientific reporting and transfer to changed inputs. Case-to-case differences can reflect different structural requirements as well as robustness; three cases do not support a generalization-rate estimate. An apparent price/score trade-off in the resource figure is descriptive and is not a compute-controlled efficiency frontier.', '',
              'The development process targeted lower Flash scores through harder scientific requirements, which introduces task-selection bias. Once frozen, every prospective configuration received the same files and prompt and the same evaluation rules. No post hoc scaling was used to force a requested score. The five resumed results additionally depend on partial original context and neutral follow-up messages. A future confirmatory study should use fresh undisclosed instances, uninterrupted prospective runs for every configuration and independent repeats and reviewers.', '',
              'Read the full [limitations](LIMITATIONS.md), [scoring policy](TASK_AND_SCORING.md), [execution protocol](EVALUATION_PROTOCOL.md) and [provenance summary](../../results/v2/run_provenance.json) before reusing a rank or figure. The protected organizer package is required to rerun official hidden scoring. Public validation establishes published-artifact consistency, not an independent replication of scientific judgment.', '']
    (ROOT / 'docs/v2/RESULTS.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f'Wrote analysis of {len(rows)} finalized configurations.')

if __name__ == '__main__':
    main()
