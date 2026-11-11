"""仅演示文件读取；分析方法自行实现。"""
from pathlib import Path
import pandas as pd

p=Path('data')
print(pd.read_csv(p/'phenotypes.tsv',sep='\t').head())
print(pd.read_csv(p/'gene_catalog.tsv',sep='\t').head())
print((p/'cohort_variants.vcf').read_text().splitlines()[:10])
