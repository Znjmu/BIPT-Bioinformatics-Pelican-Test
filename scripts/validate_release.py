#!/usr/bin/env python3
"""Validate published BIPT v1.0 release files; requires Python standard library only.

This checks internal consistency of *published scores*, not scientific correctness
of an unreleased candidate's run or the validity of the underlying rubric.
"""
from __future__ import annotations
import csv, json, math, statistics, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_FILE = ROOT / 'results' / 'leaderboard.csv'
JSON_FILE = ROOT / 'results' / 'score_details.json'
MANIFEST_FILE = ROOT / 'results' / 'submission_manifest.csv'
FIGURES = [ROOT / 'figures' / 'leaderboard.png', ROOT / 'figures' / 'public_vs_hidden.png']


def check(condition: bool, message: str):
    if not condition:
        raise AssertionError(message)


def main():
    with CSV_FILE.open(encoding='utf-8-sig', newline='') as fh:
        rows = list(csv.DictReader(fh))
    scores = json.loads(JSON_FILE.read_text(encoding='utf-8'))
    check(len(rows) == 11, f'Expected 11 leaderboard rows, got {len(rows)}')
    check(scores.get('n_archives') == 11, 'JSON: n_archives != 11')
    check(scores.get('n_valid_submissions') == 10, 'JSON: n_valid_submissions != 10')
    check(len(scores.get('results', [])) == 11, 'JSON: unexpected results length')
    score_by_id = {x['id']: x for x in scores['results']}
    check(len(score_by_id) == 11, 'Non-unique JSON result identifiers')

    valid_scores = []
    for row in rows:
        identifier = row['id']
        check(identifier in score_by_id, f'Missing JSON result for {identifier}')
        ref = score_by_id[identifier]
        check(row['model'] == ref['model'], f'Model name mismatch: {identifier}')
        check(row['score_status'] == ref['score_status'], f'Status mismatch: {identifier}')
        recorded = float(row['score'])
        check(math.isclose(recorded, float(ref['score']), abs_tol=0.011),
              f'Score mismatch for {identifier}')
        for stem in ('public_science', 'hidden1_science', 'hidden2_science'):
            check(math.isclose(float(row[stem]), float(ref[stem]), abs_tol=0.001),
                  f'Scientific score mismatch {identifier}:{stem}')
        if row['score_status'] == 'valid':
            valid_scores.append(recorded)
            # Weighted category sums should agree after official rounding.
            cats = ('annotation_35','qc_13','haplotype_23','prioritization_14',
                    'interpretation_8','reexecution_4','integrity_3')
            sub_total = sum(float(row[k]) for k in cats)
            check(abs(sub_total - recorded) < 0.026,
                  f'Weighted components disagree with score for {identifier}')
            check(row['runnable_all'].lower() == 'true',
                  f'A claimed valid run did not replay successfully: {identifier}')
        else:
            check(row['score_status'] == 'missing_delivery', 'Unexpected invalid status')
            check(recorded == 0.0, 'Historical missing result should be raw 0')

    check(len(valid_scores) == 10, 'Expected 10 valid scores')
    assert abs(statistics.mean(valid_scores)-93.51)<.01
    assert abs(statistics.median(valid_scores)-93.25)<.01
    assert abs(statistics.pstdev(valid_scores)-2.86)<.02
    assert abs(max(valid_scores)-99.62)<1e-6
    assert abs(min(valid_scores)-89.58)<1e-6
    # Check competition ranks (1, 2, 3, 3, ..., 8), treating missing as N/A.
    for row in rows:
        if row['score_status'] != 'valid': continue
        expected_rank = 1 + sum(s > float(row['score']) for s in valid_scores)
        check(expected_rank == int(row['rank']), f'Rank mismatch: {row["id"]}')

    with MANIFEST_FILE.open(encoding='utf-8-sig', newline='') as fh:
        manifest = list(csv.DictReader(fh))
    check(len(manifest) == 11, 'Manifest count mismatch')
    check(set(x['id'] for x in manifest) == set(score_by_id), 'Manifest IDs mismatch')

    for figure in FIGURES:
        check(figure.exists(), f'Missing figure: {figure}')
        with figure.open('rb') as fh:
            check(fh.read(8) == b'\x89PNG\r\n\x1a\n',f'Invalid PNG signature: {figure}')

    task = ROOT / 'benchmark' / 'Leaf_Pigment_Genetics'
    for expected in ('PROJECT_REQUEST.md','DATA_DICTIONARY.md','RESULT_FORMAT.md',
                     'PROJECT_REQUEST_EN.md','DATA_DICTIONARY_EN.md','RESULT_FORMAT_EN.md'):
        check((task/expected).is_file(), f'Missing task document: {expected}')
    for expected in ('draft_reference.fa','genes.gff3','cohort_variants.vcf',
                     'phenotypes.tsv','gene_catalog.tsv'):
        check((task/'data'/expected).is_file(),f'Missing task data: {expected}')
    for required in ('README.md','NOTICE.md','ACKNOWLEDGEMENTS.md','docs/RESULTS.md','docs/SCORING.md',
                     'docs/LIMITATIONS.md','docs/REPRODUCIBILITY.md'):
        check((ROOT/required).exists(),f'Missing required documentation: {required}')

    print('PASS: 11 entries, 10 valid, 1 missing; rankings and score totals agree.')
    print('Score summary (10 valid): mean={:.2f}, median={:.2f}, population SD={:.2f}, range={:.2f}–{:.2f}'.format(
        statistics.mean(valid_scores), statistics.median(valid_scores), statistics.pstdev(valid_scores),
        min(valid_scores), max(valid_scores)))
    print('Figures and source dataset: present.')
    print('This is an artifact integrity check, NOT an independent scientific review.')


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f'FAIL: {error}',file=sys.stderr)
        sys.exit(1)
