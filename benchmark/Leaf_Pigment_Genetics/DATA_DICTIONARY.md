# 数据字段说明

`draft_reference.fa`：scaffold 的 DNA 正向参考序列，坐标按照 FASTA 第一个字符起始计算。`genes.gff3` 使用 GFF3 标准的 1-based 闭区间；CDS 的第 8 列是 phase，不是蛋白位点。转录本区段按 CDS 所在链方向拼接。

`cohort_variants.vcf`：VCF 4.2 格式，含 REF、一个或多个 ALT、FILTER、以及每份材料的 `GT:DP:GQ`。ALT 编号从 1 起，GT 中的 `|` 与 `/` 保留其标准语义；VCF 中 POS 为 1-based 位置。所有提交结果必须使用原始记录 ID 和 ALT 的原始编号。

`phenotypes.tsv`：`sample_id` 表示基因型对应的独立材料，`assay_repeat` 表示一次色素测定；`visual_class` 为 `pale` / `green`，两类材料都属于同一物种、二倍体。

`gene_catalog.tsv`：`primary_transcript_id` 是主要表达转录本；`secondary_transcript_id` 可以为空，`primary_isoform_fraction` 是主要转录本使用比例的实验估计。

小规模试验的调用规范：只有 `FILTER=PASS`、与 FASTA 参考等位基因一致、且该材料 `DP >= 10`、`GQ >= 20` 的调用用于可信遗传负担评估。不满足者仍需保留质控记录和注释记录。没有功能验证时，序列预测与表型共分离不能等同于已证实因果机制。
