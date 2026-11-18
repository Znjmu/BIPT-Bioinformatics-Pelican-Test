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
    cases = read('case_scores.csv')
    reviews = read('scientific_review.csv')
    lines = [
        '# BIPT v2.0 — observed results and interpretation', '',
        f'The released dataset contains {len(rows)} finalized configurations: {len(completed)} completed scored submissions and {len(incomplete)} externally incomplete submissions. One uncontaminated generation was collected per configuration. The DeepSeek Flash development baseline is reused and marked with an asterisk; it is not a newly blinded run.', '',
        '**These are exact single-run observations on a selected synthetic task, not a statistically established general model ranking.** Version 1.0 scores use a different task and scale and are excluded.', '',
        '## Scores and case transfer', '',
        '| Configuration | Total / 100 | Numerical / 60 | Scientific / 35 | Delivery / 5 | Released | Held-out 1 | Held-out 2 |',
        '|---|---:|---:|---:|---:|---:|---:|---:|'
    ]
    for r in completed:
        name = r['model'] + (' *' if r['role'] == 'development_calibration_baseline' else '')
        values = [f'{fnum(r,k):.2f}' for k in ['total','numerical','scientific','delivery','public_total','hidden1_total','hidden2_total']]
        lines.append('| '+name+' | '+' | '.join(values)+' |')
    for r in incomplete:
        lines.append(f"| {r['model']} ({r['status']}) | NA | NA | NA | NA | NA | NA | NA |")
    lines += ['', 'Case totals are unweighted 100-point case scores; component columns are weighted across cases. The final total uses 20% released and 40% for each held-out case. NA means externally incomplete, not zero capability. A normal service completion can still fail a hidden replay and receive its actual frozen artifact points.', '',
              '![Component scores and case outcomes](../../figures/v2/score_and_case_comparison.png)', '']
    lines += [f'**Completion coverage:** only {sum(r["role"]=="prospective_comparison" for r in completed)} of the seven fresh configurations reached normal service completion within their predeclared limits. The five externally stopped configurations do not have completed ability scores. Thus the planned broad score comparison and two provider pairs remain unresolved; the released evidence supports a limited completed-submission comparison plus an all-configuration service-outcome comparison.', '']
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
    lines += ['Differences compare the same three fixed cases. They do not isolate a causal speed-tier effect: DeepSeek and MiniMax labels also differ in version, GLM standard has no Pro suffix, practical credit ceilings differ, and the DeepSeek Flash result helped select task difficulty. An unavailable completed pair remains NA. No significance test or confidence interval is attached.', '',
              '![Matched-case differences and actual resource observations](../../figures/v2/paired_and_resource_comparison.png)', '',
              '## Execution and resource observations', '', '![All actual service costs, including externally interrupted runs](../../figures/v2/execution_resources.png)', '', '| Configuration | Status | Credits | Service minutes | Successful case exits |', '|---|---|---:|---:|---:|']
    for r in rows:
        successes = sum(int(x['returncode']) == 0 for x in cases if x['configuration_id'] == r['configuration_id'])
        exits = f'{successes}/3' if r['status'] == 'completed_scored' else 'NA'
        lines.append(f"| {r['model']} | {r['status']} | {fnum(r,'credits'):.2f} | {fnum(r,'elapsed_seconds')/60:.1f} | {exits} |")
    lines += ['', f"New comparison runs plus declared operator overhead consumed {details['new_comparison_credits_settled']:.2f} settled WorkBuddy credits. The reused Flash baseline's 38.28 credits belong to its earlier development run. Operator overhead is {details['operator_overhead_credits']:.2f} credits and is excluded from model scores.", '',
              'The authorized combined comparison allowance was 1494.28 credits; 377.04 remained after all seven fresh main runs settled. The optional Kimi Pro run was not activated because the predeclared eligibility threshold was 400 remaining credits. These values describe this release\'s settled ledger, not the account balance.', '',
              'Credits are observed service bills, not tokens or matched compute. All new jobs have a 60-minute external service allowance with predeclared model-specific credit stops. At most two generation jobs overlap; final scoring reruns are serial with 360 seconds per case. See [the disclosed plan](../../results/v2/comparison_plan.csv).', '',
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
              'The development process targeted lower Flash scores through harder scientific requirements, which introduces task-selection bias. Once frozen, every prospective configuration received the same files and prompt and the same evaluation rules. No post hoc scaling was used to force a requested score. A future confirmatory study should use fresh undisclosed instances, prospective runs for every configuration and independent repeats and reviewers.', '',
              'Read the full [limitations](LIMITATIONS.md), [scoring policy](TASK_AND_SCORING.md), [execution protocol](EVALUATION_PROTOCOL.md) and [provenance summary](../../results/v2/run_provenance.json) before reusing a rank or figure. The protected organizer package is required to rerun official hidden scoring. Public validation establishes published-artifact consistency, not an independent replication of scientific judgment.', '']
    (ROOT / 'docs/v2/RESULTS.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f'Wrote analysis of {len(rows)} finalized configurations.')

if __name__ == '__main__':
    main()
