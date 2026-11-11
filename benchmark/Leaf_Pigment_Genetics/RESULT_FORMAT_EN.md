# Result data integration schema — English translation

*Informational translation of `RESULT_FORMAT.md` supplied in Chinese in the historical round. **Use the original output filenames, columns, and keys** listed below.*

Write all files directly under the output directory supplied to `run.sh`. TSV files must use UTF-8 encoding. **Keep exact filenames and column names**; output row ordering is unrestricted.

## 1. `variant_consequences.tsv`

For every VCF record, provide the consequence of each ALT allele for every relevant transcript. For records with no adjacent CDS, use `transcript_id=.` and `gene_id=.`.

Columns in order:

`variant_id`, `alt_index`, `transcript_id`, `gene_id`, `effect`

`alt_index` is the 1-based index of the corresponding ALT in the original VCF.

`effect` must be one of:

`ref_mismatch`, `intergenic`, `intronic`, `splice_site`, `synonymous`, `missense`, `start_lost`, `stop_gained`, `stop_lost`, `frameshift`, `inframe_indel`.

For coding variants, assess effects by translating reference and alternate CDS sequence. For noncoding variants adjacent to a splice boundary, `splice_site` refers here to the 2-nt donor/acceptor boundary. Complex isoform splicing, 3D protein structural effects, and actual enzyme activity are beyond scope.

## 2. `variant_qc.tsv`

One row per original VCF record:

`variant_id`, `reference_matches`, `site_pass`, `n_high_confidence_carriers`

`reference_matches`: boolean indicating whether REF matches the supplied FASTA at the VCF position.

`site_pass`: true only if genomic REF is correct **and** VCF `FILTER=PASS`.

`n_high_confidence_carriers`: number of **unique independent accessions** meeting the DP and GQ requirements and containing at least one ALT genotype, only for passing variant sites. A sample with `1|2` at a multiallelic site counts as **one carrier**, not two.

## 3. `accession_gene_burden.tsv`

One row per VCF accession × gene in `gene_catalog.tsv`:

`sample_id`, `gene_id`, `disrupted_haplotypes`, `biallelic_disruptive`

`disrupted_haplotypes` is the count (0, 1, or 2) of haplotypes that carry at least one **high-confidence** `stop_gained`, `frameshift`, or `start_lost` variant on the **primary transcript**. Multiple disruptive variants on a single haplotype count as **one disrupted haplotype**.

`biallelic_disruptive` is `true` if and only if `disrupted_haplotypes == 2`. Report definitive haplotype burden only for sufficiently interpretable phased calls; do not assume unphased calls are trans.

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

Replace each `null` with a **computed** result. `inheritance_model` is one of `recessive_biallelic`, `dominant_single_allele`, or `no_supported_model`.

`causality_established` is a boolean asking whether the supplied evidence **proves** a phenotype-causing mechanism. `case_biallelic` and `control_biallelic` are the numbers of independent `pale` and `green` accessions, respectively, with predicted biallelic disruption in the selected gene.

`supporting_variant_ids` is a list of high-confidence disruptive variant IDs on the chosen gene's **primary transcript**.

## 5. Figure and interpretation

- `segregation.png`: minimum **850×450** pixels; include a title, gene/accession labeling, axes, and core segregation evidence.
- `interpretation.md`: a concise discussion of the results, the strength of the evidence, and outstanding needs for validation (recommended **150–400 Chinese characters** in the original request; a comparable concise English note is sufficient for this translation).
