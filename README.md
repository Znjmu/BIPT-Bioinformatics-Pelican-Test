# BIPT v2.0｜给 AI 做一场生信推理考试

**给不同 AI 同一份题，让它们各自写代码、算结果、解释结论，再用同一套规则和同一个固定评分模型打分。** 你不必先看懂全部数学，照下面操作就能开始试跑。

## 第一次来？先选你要做什么

| 你想做什么 | 直接点这里 |
|---|---|
| **我想拿一个模型试试** | **[① 下载参测包](https://github.com/Znjmu/BIPT-Bioinformatics-Pelican-Test/releases/download/v2.0/BIPT_v2.0_participant.zip)** → **[② 打开要发给模型的任务提示](docs/v2/PARTICIPANT_PROMPT.md)** |
| 我想一步一步照着做 | **[打开傻瓜式操作指南](docs/v2/QUICK_START.md)** |
| 我只想先读懂原理 | **[读约 400 字的通俗说明](docs/v2/PLAIN_GUIDE_ZH.md)** |
| 我想看谁得分高、为什么扣分 | [中文实测分析和对比图](docs/v2/RESULTS_ZH.md) |
| 我是负责评分的人 | [打开固定评分者提示](docs/v2/GRADING_AGENT_PROMPT.md)；还需要组织者提供的私有评分包 |
| 我想下载全部公开资料 | [v2.0 正式发布页](https://github.com/Znjmu/BIPT-Bioinformatics-Pelican-Test/releases/tag/v2.0) |

> **最容易拿错的两个文件：**
> - **任务提示**＝考卷要求，发给**待测模型**。参测 ZIP 中的 `PARTICIPANT_PROMPT.txt` 就是同一段提示。
> - **评分提示**＝阅卷要求，只发给**固定评分者**。不要发给待测模型，也不要把整仓库交给它。

## 它到底考什么？

可以把它想成：给 AI 一批虚拟生物样本的检测线索，让它找出“哪些情况说得准、哪些只能给范围、哪些根本无法判断”，再选一个满足题目风险限制的实验方案。题里故意放入容易混淆的情况，例如同一样本重复测量、不同样本抽取，以及整场实验共用的检测偏差。AI 既要算对，也要把证据和结论讲对。

数据全部为合成数据。题中的“伤害”和“安全”是数学实验里的定义，不能直接解释成真实临床疗效或安全性。这套测试反映模型在本题上的表现。

## 用 WorkBuddy，照这 5 步做

1. **建空文件夹。** 每个模型单独建一个，例如“模型A_第1次”“模型B_第1次”。每次新试跑也用新文件夹、新任务会话。
2. **解压参测包。** 只解压上面下载的 `BIPT_v2.0_participant.zip`。应看到 `Finite_Panel_Rescue` 文件夹和 `PARTICIPANT_PROMPT.txt`。
3. **选目录、选模型、发任务。** 在 WorkBuddy 打开对应工作目录，确认实际模型名称。打开 `PARTICIPANT_PROMPT.txt`，全文复制到输入框，发送一次。不同模型收到完全相同的内容。
4. **等它做完，原样保存。** 保留整个项目和完成状态，记下模型名称、用时、积分及中断情况。代码和结果先归档，不替模型修正；失败的尝试也保留。
5. **交给同一个固定评分模型。** 把原始项目交给评分者，由它按统一规则复跑、检查科学解释和图片，最后汇总。具体材料和常见问题见[操作指南](docs/v2/QUICK_START.md)。

> **公平规则：所有待评估模型的产物，都交给同一个固定评分模型，使用相同的评分提示、评分程序、隐藏题、运行环境和科学审核标准。** 不给某个模型额外答案或纠错提示。

## 分数怎么来的？

| 每套题满分 100 分 | 怎么检查 |
|---|---|
| **算得对：60 分** | 冻结的评分程序核对数值、约束、方案和证明材料 |
| **讲得对：35 分** | 同一个固定评分模型逐项核对本题证据、报告和图片；明确科学错误，该项为 0 分，同一错误不重复扣 |
| **能复跑、交得全：5 分** | 原代码能否正常运行并产出全部 14 项要求文件 |

一个模型会在 **1 套公开题＋2 套隐藏题** 上复跑原代码，最终分数是：**公开题 × 20%＋隐藏题 1 × 40%＋隐藏题 2 × 40%**。隐藏题检查代码能否处理换过的数据，避免只记住公开答案。科学解释未审完，不能把程序算出的部分分数当成最终总分。

**只有公开包，也能试跑；要得到完整正式评分，还需要组织者保存的私有评分包。** 该包包含隐藏输入、参考答案和评分程序，不在公开仓库。公开的检查脚本只检查已发布资料是否一致，不能代替正式评分。

---

下面保留详细结果和技术资料，第一次使用可先读到这里。

## Results and analysis

**[中文完整实测分析 →](docs/v2/RESULTS_ZH.md)** · **[Full English analysis →](docs/v2/RESULTS.md)**

![BIPT v2.0 component scores and case outcomes](figures/v2/score_and_case_comparison.png)

![Within-provider configuration differences and actual service resources](figures/v2/paired_and_resource_comparison.png)

![Initial and continuation service costs](figures/v2/execution_resources.png)

The completed comparison covers DeepSeek Pro/Flash, GLM standard/Flash, MiniMax standard/Flash, MiMo Pro and Step Preview. **All eight configurations have final scores; no generation is left as a budget-stopped NA.** GLM standard/Flash, MiniMax standard/Flash and Step were completed by resuming their original chats after generation stopping limits were removed. A plus sign marks these resumed completions; they are not independent new trials. The [historical capped results](docs/v2/HISTORICAL_CAPPED_RESULTS.md) remain available.

**Observed totals:** GLM-5.3 82.01, MiniMax-M3.1-Flash 73.89, GLM-5.3-Flash 71.41, MiniMax-M3 63.01, Xiaomi MiMo-V2.6-Pro 58.53, DeepSeek-V4-Pro 44.25, Step-5-Preview 40.03, DeepSeek-V4.1-Flash 38.65. See the [full analysis](docs/v2/RESULTS.md) for component scores, all three cases, provider-pair differences, execution exits and scientific deductions.

**The reused DeepSeek-V4.1-Flash result is a development/calibration baseline**, marked with an asterisk. Its feedback helped select task difficulty, so it is not a newly blinded comparator. There is one original generation per configuration, with disclosed neutral continuation messages for five. No confidence interval, significance test or general model-superiority claim is inferred. Cross-version provider labels and different inference resources prevent a causal speed-tier or matched-compute conclusion.

The completion follow-up used the same frozen inputs, rubric, evaluator and 360-second per-case grading limit, without scientific feedback to participating models. Model service completion and successful hidden replay are separate outcomes. The optional Kimi configuration is outside this eight-configuration follow-up.

## What changed in v2.0

| Area | v2.0 behavior |
|---|---|
| Scientific task | Finite clonal-panel inference and rescue design, using exact synthetic technical expectations. |
| Evidence reconciliation | Single reads, same-member cloned pairs and distinct-member selected pairs must agree with a common integer panel. |
| Shared technical noise | One unobserved batch persists for the full experiment; conditioning and path integration must preserve it. |
| Identification | Distinguish point, partial and undefined queries; compare physical integer bounds with a specified symmetric-pair outer relaxation. |
| Experimental decisions | Audit all protocol paths and optimize one common randomized design under overall and layer-specific risk constraints. |
| Mathematical proof | Deliver physical witnesses and valid tight global vector certificates; accept non-unique valid solutions. |
| Scientific scoring | Ten evidence-grounded R01–R10 items; explicit scientific errors receive zero for the corresponding item. Correct tables do not erase contradictory prose. |
| Transfer testing | Re-execute unchanged submitted code on the released case and two held-out cases, weighted 20% / 40% / 40%. |
| Reporting | Separate score components, execution failures, external stops, operator overhead, actual credits and elapsed time. |

The difficulty target was used during development to add substantive requirements. **Frozen evaluation scores are not adjusted to reach a desired number.** Read [the task and scoring guide](docs/v2/TASK_AND_SCORING.md) for the exact categories and [limitations](docs/v2/LIMITATIONS.md) for calibration bias and other boundaries.

## Data and reproducibility

| Material | Location |
|---|---|
| Released task, data dictionary and output contract | [Finite_Panel_Rescue](benchmark/Finite_Panel_Rescue/) |
| Byte-identical participant prompt | [Participant prompt](docs/v2/PARTICIPANT_PROMPT.md) |
| Fixed-evaluator procedure | [Evaluator prompt](docs/v2/GRADING_AGENT_PROMPT.md) |
| Execution, scoring and interpretation policy | [Evaluation protocol](docs/v2/EVALUATION_PROTOCOL.md) |
| Totals and components | [leaderboard.csv](results/v2/leaderboard.csv) |
| Case-level scores and replay exits | [case_scores.csv](results/v2/case_scores.csv) |
| All scientific item points and safe deduction summaries | [scientific_review.csv](results/v2/scientific_review.csv) |
| Historical initial caps and outcomes | [comparison_plan.csv](results/v2/comparison_plan.csv) |
| Initial and continuation costs, service durations and neutral messages | [execution_phases.csv](results/v2/execution_phases.csv) |
| Exact shared neutral continuation instruction | [Continuation prompt](docs/v2/CONTINUATION_PROMPT.md) |
| Freeze hashes, runtime and archive provenance | [run_provenance.json](results/v2/run_provenance.json) |
| Figure source | [R plotting script](scripts/plot_v2_results.R) |
| Editable and preview figures | [PDF, SVG and 600-dpi PNG](figures/v2/) |

To check the published tables, score arithmetic, public task hashes and exported figure files:

```bash
python3 scripts/validate_v2_release.py
```

To regenerate the comparison figures from the published result tables, use R with `ggplot2`, `svglite`, `ggrepel` and `ragg` installed:

```bash
Rscript scripts/plot_v2_results.R
python3 scripts/write_v2_analysis.py
```

These are **published-artifact checks**, not a reproduction of hidden scoring or an independent scientific review. The protected organizer package contains the hidden inputs, reference answers and grading implementation and remains organizer-held. Without that package, readers can try the public task and verify published consistency, but cannot claim a new official hidden-case score.

The participant's executable contract is:

```bash
bash run.sh INPUT_DIR OUTPUT_DIR
```

`INPUT_DIR` directly contains the supplied TSV/JSON inputs; `OUTPUT_DIR` must not exist beforehand. The full [output specification](benchmark/Finite_Panel_Rescue/RESULT_FORMAT.md) requires fourteen artifacts. Separate working directories are workflow isolation, not an operating-system security boundary.

## Historical release and project scope

The [v1.0 README](README_v1.0.md), original [v1.0 results](results/leaderboard.csv), plant-genetics task and plotting scripts remain available. **Do not merge v1.0 and v2.0 leaderboards or interpret their score difference as a model improvement or decline.** The historical v1.0 hash manifest is preserved separately as [SHA256SUMS_v1.0.txt](SHA256SUMS_v1.0.txt).

“Pelican” is an informal project name. All inputs are synthetic; this is not clinical evidence, an experimental validation claim or an official standardized benchmark. **All results and interpretations represent the author's views only.** The project is independent of, and is not endorsed or certified by, any listed model provider, university, journal or other institution.

Special thanks to **[BioMamba Bioinformatics Base / Biomamba 生信基地](https://biomamba.top/index.html)** for public bioinformatics education. This acknowledgment does not imply participation in or endorsement of the evaluation. See [Acknowledgments](ACKNOWLEDGEMENTS.md), [Notice](NOTICE.md) and [release notes](RELEASE_NOTES.md).
