#!/usr/bin/env python3
"""Check published v2.0 result arithmetic, provenance and artifacts; not a new scientific review."""
from pathlib import Path
import csv,json,math,hashlib,sys,re,zipfile
ROOT=Path(__file__).resolve().parents[1];R=ROOT/'results/v2'
def table(name):
 with (R/name).open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))
def check(ok,message):
 if not ok:raise AssertionError(message)
def main():
 d=json.loads((R/'score_details.json').read_text());rows=table('leaderboard.csv');cases=table('case_scores.csv');reviews=table('scientific_review.csv');by={r['configuration_id']:r for r in rows};expected={'DS_FLASH_DEV',*[f'R{i:02}' for i in range(1,8)]};check(set(by)>=expected,'Main comparison configurations not all finalized');check(len(by)==len(rows)==d['n_finalized_configurations'],'Duplicate/count mismatch');check(d['reviewer_id']=='Codex-primary-common-evaluator','Evaluator mismatch');check(d['weights']=={'public':.2,'hidden1':.4,'hidden2':.4},'Case weights changed');check(d['development_baseline_selection_bias'] is True,'Development limitation missing')
 jby={r['configuration_id']:r for r in d['results']};check(set(jby)==set(by) and len(jby)==len(d['results']),'JSON/CSV configuration mismatch')
 for r in rows:
  jr=jby[r['configuration_id']];check(r['status'] in ['completed_scored','incomplete_settled','provider_failure_settled'],'Unfinalized status in published results')
  check(all(r[k]==jr[k] for k in ['model','family','tier','role','status']),'JSON/CSV identity mismatch')
  for k in ['credits','elapsed_seconds','fee_multiplier','total','numerical','scientific','delivery']:
   check((r[k]=='' and jr[k] is None) or (r[k]!='' and jr[k] is not None and abs(float(r[k])-float(jr[k]))<1e-6),'JSON/CSV numeric mismatch: '+k)
  rid=r['configuration_id'];check(int(r['generation_replicates'])==1,'Incorrect generation replicate count');check(float(r['credits'])>=0 and float(r['elapsed_seconds'])>=0,'Invalid resource observation');cr=[x for x in cases if x['configuration_id']==rid];sr=[x for x in reviews if x['configuration_id']==rid]
  if r['status']!='completed_scored':check(r['total']=='' and not cr and not sr,'Incomplete run incorrectly given completed scores');continue
  check(len(cr)==3 and {x['case'] for x in cr}==set(d['weights']),'Incomplete/duplicate scored case rows');check(len(sr)==30,'Missing scientific item audit');check(abs(sum(float(r[k]) for k in ['numerical','scientific','delivery'])-float(r['total']))<=.00501,'Component total mismatch');check(len(r['source_score_sha256'])==64,'Missing score digest')
  weighted=0.;component={k:0. for k in ['numerical','scientific','delivery']}
  for x in cr:
   check(abs(float(x['case_weight'])-d['weights'][x['case']])<1e-9,'CSV case weight changed')
   check(all(0<=float(x[k])<=mx for k,mx in [('numerical',60),('scientific',35),('delivery',5)]),'Case component out of bounds');check(abs(sum(float(x[k]) for k in component)-float(x['total']))<1e-6,'Case total mismatch');check(int(x['returncode'])==0 or float(x['delivery'])==0,'Nonzero exit credited full delivery');items=[y for y in sr if y['case']==x['case']];check({y['item'] for y in items}=={f'R{i:02}' for i in range(1,11)},'Review items changed');check(all(float(y['points']) in [0,1.75,3.5] for y in items),'Review point scale changed');check(abs(sum(float(y['points']) for y in items)-float(x['scientific']))<1e-6,'Review/case mismatch');weighted+=d['weights'][x['case']]*float(x['total'])
   for k in component:component[k]+=d['weights'][x['case']]*float(x[k])
  check(abs(weighted-float(r['total']))<=.00501,'Weighted case total mismatch')
  for k in component:check(abs(component[k]-float(r[k]))<1e-5,'Weighted component mismatch')
 if d.get('completion_followup'):
  check(len(rows)==8 and all(r['status']=='completed_scored' for r in rows),'Completion release contains unfinished configurations')
  check(d['all_generation_tasks_normally_completed'] and d['all_case_replays_attempted'],'Completion/replay status unclear')
  check(all((r['all_case_entries_succeeded'].lower()=='true')==all(int(x['returncode'])==0 for x in cases if x['configuration_id']==r['configuration_id']) for r in rows),'Case entry success flag mismatch')
  check(d['credit_limits_removed_by_user'] and d['generation_credit_cap_completion_phase'] is None and d['generation_wall_clock_cap_completion_phase'] is None,'Completion limits incorrectly reported')
  ph=table('execution_phases.csv');check(len(ph)==8 and {x['configuration_id'] for x in ph}==set(by),'Missing phase accounting')
  for x in ph:
   r=by[x['configuration_id']]
   for suffix in ['credits','elapsed_seconds']:
    check(abs(float(x['initial_'+suffix])+float(x['continuation_'+suffix])-float(x['total_'+suffix]))<1e-6,'Initial/continuation sum mismatch')
    check(abs(float(x['total_'+suffix])-float(r[suffix]))<1e-6,'Phase/main resource mismatch')
   resumed=r['role']=='completion_after_external_interruption'
   check(int(x['neutral_continuation_messages'])>=1 if resumed else int(x['neutral_continuation_messages'])==0,'Neutral-message role mismatch')
  check(abs(sum(float(x['continuation_credits']) for x in ph)-d['completion_phase_credits'])<1e-6,'Completion cost mismatch')
  fresh=sum(float(x['total_credits']) for x in ph if x['configuration_id']!='DS_FLASH_DEV')+d['operator_overhead_credits']
  check(abs(fresh-d['new_comparison_credits_settled'])<1e-6,'Comparison cost mismatch')
  check(abs(d['original_capped_phase_credits']+d['completion_phase_credits']-d['new_comparison_credits_settled'])<1e-6,'Overall phase total mismatch')
  prov=json.loads((R/'run_provenance.json').read_text());cp=prov['completion_followup']
  prompt=(ROOT/'docs/v2/CONTINUATION_PROMPT.md').read_bytes()
  check(hashlib.sha256(prompt).hexdigest()==cp['common_neutral_prompt_sha256']==d['neutral_continuation_prompt_sha256'],'Neutral prompt changed')
  check(cp['same_frozen_task_and_grader'] and cp['case_replay_timeout_seconds']==360 and cp['no_hidden_feedback_or_scientific_corrections'],'Completion evaluation provenance missing')
  check(len(cp['runs'])==5 and all(x['final_status']=='completed_scored' and not x['source_repaired_by_evaluator'] for x in cp['runs']),'Resumed original projects incomplete')
  hist=table('history_capped/leaderboard.csv');check(sum(x['status']!='completed_scored' for x in hist)==5,'Capped history lost')
 released_hashes=json.loads((R/'released_input_hashes.json').read_text())
 for rel,digest in released_hashes.items():
  p=ROOT/'docs/v2/PARTICIPANT_PROMPT.md' if rel=='PARTICIPANT_PROMPT.txt' else ROOT/'benchmark'/rel
  check(p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==digest,'Released task input differs from freeze: '+rel)
 with zipfile.ZipFile(ROOT/'releases/BIPT_v2.0_participant.zip') as z:
  check(len(z.namelist())==len(released_hashes) and set(z.namelist())==set(released_hashes),'Participant ZIP has extra/missing files')
  check(all(hashlib.sha256(z.read(k)).hexdigest()==v for k,v in released_hashes.items()),'Participant ZIP differs from released files')
 for stem in ['score_and_case_comparison','paired_and_resource_comparison','execution_resources']:
  p=ROOT/'figures/v2'/stem
  check(p.with_suffix('.png').read_bytes()[:8]==b'\x89PNG\r\n\x1a\n','Missing/invalid PNG');check(p.with_suffix('.pdf').read_bytes().startswith(b'%PDF-'),'Missing/invalid PDF');check('<text' in p.with_suffix('.svg').read_text(),'SVG text is not editable')
 for base in ['docs/v2','results/v2','benchmark/Finite_Panel_Rescue']:
  for p in (ROOT/base).rglob('*'):
   if not p.is_file():continue
   check(not any(s in p.name for s in ['PRIVATE','organizer_private','generator_counts']),'Private file in public payload')
   if p.suffix in ['.md','.json','.csv','.txt']:
    check(not re.search(r'wbSeedToken|accountSnapshot|/Users/z/|/tmp/bipt_',p.read_text()),'Private/account metadata leaked: '+str(p.relative_to(ROOT)))
 print(f'PASS v2.0: {len(rows)} finalized configurations; case/component/review arithmetic and public task hashes agree.')
 print('Published-artifact QA only; private scientific scoring requires the organizer package.')
if __name__=='__main__':
 try:main()
 except Exception as exc:print('FAIL:',exc,file=sys.stderr);sys.exit(1)
