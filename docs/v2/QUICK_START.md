# Beginner guide / 傻瓜式操作指导

## Start with these two prompts / 先看这两个入口

| Give the participant / 发给待测模型 | Give the fixed evaluator / 发给固定评估者 |
|---|---|
| **[① TASK PROMPT / 任务提示](PARTICIPANT_PROMPT.md)** | **[② EVALUATOR PROMPT / 评分提示](GRADING_AGENT_PROMPT.md)** |

**[DOWNLOAD THE PARTICIPANT ZIP / 下载参测包](../../releases/BIPT_v2.0_participant.zip)**

The evaluator also needs the protected organizer scoring package. It contains hidden inputs and reference answers and is **not included in the public repository**. Do not give that package to a participant.

## Five steps

1. **Make a new folder for each model.** In your project area, create a separate empty folder such as `BIPT20_ModelName_Trial1`. A different model or attempt needs a different folder.
2. **Extract only the participant ZIP there.** It contains `Finite_Panel_Rescue/` and `PARTICIPANT_PROMPT.txt`. Do not give an agent the entire GitHub repository: results, evaluator instructions and other submissions are not participant context.
3. **Open that folder in WorkBuddy.** Select the intended built-in model. Copy the complete participant prompt without edits and send it once. Record the exact visible model name, fee multiplier, start time and agreed external time/credit limit. Use the same task/prompt for all models; do not help one model with corrective follow-ups.
4. **Collect the whole project.** Wait for the service to finish, save its original code and outputs, and record actual elapsed time and credits. Keep failed and incomplete attempts too. Do not fix code before archiving. An operator mistake must be declared and excluded; a clean replacement must use a new directory.
5. **Grade everything with one fixed evaluator.** Give all original projects to the same evaluator configuration, the same organizer package and the evaluator prompt. It reruns all three cases, reads the actually delivered scientific reports and images, and reports numerical/scientific/delivery components separately. Read failure labels and limitations before comparing totals.

**Fairness rule: all model artifacts must go to the same evaluation model, with the same frozen task, scoring software, hidden cases, runtime and scientific-review rules.** The v2.0 35-point scientific component uses evidence-grounded evaluator judgment; an automatic numerical score is not yet a final total.

## 中文逐步说明

1. 在“工程”下给每个模型建一个全新文件夹；不同模型、不同试次不要共用目录。
2. 只把上面的**参测包**解压进去。文件夹里应有`Finite_Panel_Rescue`和`PARTICIPANT_PROMPT.txt`，不要把整个仓库、评分材料或旧答案一起交给模型。
3. 在WorkBuddy选择这个目录和要测试的内置模型，全文复制任务提示，发送一次。记下型号、费率、开始时间和预先约定的时间/积分限制，不给某个模型额外纠错提示。
4. 显示完成后保留整个项目，包括`run.sh`、源代码和产物，记录实际用时与积分；失败也保留。先归档，再评分，不替模型改代码。操作污染要单独说明并排除，干净重试使用新目录。
5. 所有模型产物交给**同一个固定评估者**，使用同一冻结私有包、同一环境和规则。先自动复跑，再逐项读科学解释并看实际图片；科学没审完只能报区间。对比时同时看总分、隐藏题、错误类型和资源消耗。

私有组织者包包含隐藏输入、答案和评分实现，不能发给待测模型。本公开仓库没有该私有包；没有它可以做公开题试跑和检查已发布数据的一致性，但不能自行声称得到官方隐藏题分数。

## Technical contract for collected code

The submitted project must provide an original entry point:

```bash
bash run.sh INPUT_DIR OUTPUT_DIR
```

For a released-case replay, `INPUT_DIR` is the supplied `Finite_Panel_Rescue` directory, which directly contains the TSV/JSON inputs. The output directory should not exist before the call. Fourteen artifacts are required; see the participant [output specification](../../benchmark/Finite_Panel_Rescue/RESULT_FORMAT.md). Hidden cases are supplied only by the organizer. A successful repeat execution is a reproducibility check, not a new independent model-generation replicate.
