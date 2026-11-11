#!/usr/bin/env python3
"""Redraw the two benchmark figures from the released leaderboard CSV.

Usage: python scripts/plot_results.py [--output-dir path/to/figures]
Requires matplotlib; uses no source or knowledge of hidden answer keys.
"""
from __future__ import annotations
import argparse,csv
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parents[1]


def shortname(row):
    names = {
        'DeepSeek V4 Pro':'DeepSeek V4 Pro',
        'GPT-6 Luna (Codex Max)':'GPT-6 Luna (Codex Max)',
        'MiniMax M3.1 Flash':'MiniMax M3.1 Flash',
        'HY4':'HY4',
        'Space-Bunny':'Space-Bunny',
        'Kimi K3.1 Pro':'Kimi K3.1 Pro',
        'GPT-6.1 Sol (Codex High)':'GPT-6.1 Sol (Codex High)',
        'GLM-5.3 Flash':'GLM-5.3 Flash',
        'Xiaomi MiMo V2.6 Pro':'Xiaomi MiMo V2.6 Pro',
        'DeepSeek V4.1 Flash':'DeepSeek V4.1 Flash',
    }
    return names.get(row['model'],row['model'])


def render(out):
    rows=list(csv.DictReader((ROOT/'results'/'leaderboard.csv').open(encoding='utf-8-sig',newline='')))
    valid=sorted([x for x in rows if x['score_status']=='valid'],key=lambda x:-float(x['score']))
    labels=[shortname(r) for r in valid]
    values=[float(r['score']) for r in valid]
    n=len(valid)
    fig,ax=plt.subplots(figsize=(13,7.7),dpi=160)
    bars=ax.barh(range(n),values)
    ax.set_yticks(range(n),labels)
    ax.invert_yaxis()
    ax.set_xlim(0,107)
    ax.set_xlabel('BIPT v1.0 total score (0–100)')
    ax.set_title('BIPT v1.0 — historical leaderboard (10 valid submissions)')
    for b,score in zip(bars,values):
        ax.text(score+0.7,b.get_y()+b.get_height()/2,f'{score:.2f}',va='center',fontsize=9)
    ax.grid(axis='x',alpha=.18)
    ax.set_axisbelow(True)
    fig.text(.12,.015,'Note: GPT-5.6 Luna Light had no analysis deliverable (N/A); it is not plotted as a scientific zero.',fontsize=8)
    fig.tight_layout(rect=(0,0.04,1,1))
    fig.savefig(out/'leaderboard_regenerated.png',bbox_inches='tight')
    plt.close(fig)

    fig,ax=plt.subplots(figsize=(12.5,7.4),dpi=160)
    y=np.arange(n)
    fields=[('public_science','Released'),('hidden1_science','Held-out 1'),('hidden2_science','Held-out 2')]
    h=.24
    for idx,(key,label) in enumerate(fields):
        ax.barh(y+(idx-1)*h,[float(r[key]) for r in valid],height=h,label=label)
    ax.set_yticks(y,labels)
    ax.invert_yaxis()
    ax.set_xlabel('Scientific score per dataset / 93')
    ax.set_xlim(0,98)
    ax.set_title('Released vs held-out scientific accuracy')
    ax.legend(loc='lower right')
    ax.grid(axis='x',alpha=.16)
    ax.set_axisbelow(True)
    fig.tight_layout()
    fig.savefig(out/'public_vs_hidden_regenerated.png',bbox_inches='tight')
    plt.close(fig)
    print('Saved:',out/'leaderboard_regenerated.png', 'and',out/'public_vs_hidden_regenerated.png')


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output-dir',default=str(ROOT/'figures'))
    args=parser.parse_args()
    output=Path(args.output_dir);output.mkdir(parents=True,exist_ok=True)
    render(output)
