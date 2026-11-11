# 数据系统对接格式

将全部文件放入传入 `run.sh` 的输出目录。所有表必须是 UTF-8 编码的 TSV，必须保留文件名与列名，行顺序不限。

## 1. `variant_consequences.tsv`

必须覆盖每条 VCF 记录的每个 ALT 对每个相关转录本的预测后果。无相邻 CDS 的记录以 `transcript_id=.`、`gene_id=.` 表示。列名：

`variant_id` `alt_index` `transcript_id` `gene_id` `effect`

`alt_index` 为 VCF ALT 列中的编号（从 1 开始）。`effect` 取值范围：

`ref_mismatch`, `intergenic`, `intronic`, `splice_site`, `synonymous`, `missense`, `start_lost`, `stop_gained`, `stop_lost`, `frameshift`, `inframe_indel`

对于编码区变异，从参考 CDS 与变异后 CDS 的预测翻译判断影响；对于剪接相邻的非编码位置，`splice_site` 指紧邻外显子的 2 nt 供体/受体边界。此处不要求推断复杂剪接异构体、蛋白三维结构或实际酶活。

## 2. `variant_qc.tsv`

每个 VCF 记录一行；列名：

`variant_id` `reference_matches` `site_pass` `n_high_confidence_carriers`

`reference_matches`：VCF REF 是否与 FASTA 对应位置一致，布尔值。`site_pass`：是否满足 REF 一致且 VCF FILTER 为 PASS。`n_high_confidence_carriers`：在 site_pass 为真时，达到 DP、GQ 门槛且 GT 至少包含 1 个 ALT 的独立材料数（多 ALT 位点的 1/2 同样是一名携带者）。

## 3. `accession_gene_burden.tsv`

每个 VCF 样本 × `gene_catalog.tsv` 内每个基因一行。列名：

`sample_id` `gene_id` `disrupted_haplotypes` `biallelic_disruptive`

`disrupted_haplotypes` 为主要转录本上，至少承载一个高置信度 `stop_gained`、`frameshift` 或 `start_lost` 的单倍型数，取 0、1、2；同时发生在同一条单倍型上的多个变异只计一个被破坏的单倍型。`biallelic_disruptive` 为 `disrupted_haplotypes == 2`，布尔值。本项仅对能判定两个单倍型的分相基因型作确定性统计，未分相或无法判定的记录不能凭空推定为反式。

## 4. `summary.json`

```json
{
  "n_independent_accessions": null,
  "n_phenotype_measurements": null,
  "top_gene_id": null,
  "top_transcript_id": null,
  "inheritance_model": null,
  "causality_established": null,
  "case_biallelic": null,
  "control_biallelic": null,
  "supporting_variant_ids": []
}
```

除 `supporting_variant_ids` 之外的字段都须由代码更新，不能原样留空。`inheritance_model` 可选择 `recessive_biallelic`、`dominant_single_allele`、`no_supported_model`。`causality_established` 是布尔值，表示现有材料能否**确证**致病/致表型因果效应；`case_biallelic` 与 `control_biallelic` 分别是选定最佳基因在 pale/green 材料中双单倍型预测失活的独立材料数；`supporting_variant_ids` 应为主要转录本上支持最佳基因推断的高置信度破坏性变异 ID 列表。

## 5. 图与说明

`segregation.png`：至少 850×450 像素，包含图题、基因或材料标签、轴说明；展示优先候选的关键遗传证据。

`interpretation.md`：简短的结果解释、证据层级与仍需验证的内容（建议 150–400 字）。
