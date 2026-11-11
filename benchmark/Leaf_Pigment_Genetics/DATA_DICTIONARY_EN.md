# Data dictionary — English translation

*Informational translation of `DATA_DICTIONARY.md`; preserve the original Chinese file for historical replay.*

**`draft_reference.fa`**: Positive-strand DNA reference sequences of the supplied scaffolds. Reference positions are counted starting with the first FASTA base. **`genes.gff3`** uses the GFF3 standard of **1-based, end-inclusive coordinates**; column 8 of a CDS feature is **phase**, not the protein position. Transcript segments must be assembled in the direction of the coding strand.

**`cohort_variants.vcf`**: VCF 4.2 with REF, one or more ALTs, site FILTER values, and per-accession `GT:DP:GQ`. ALT allele indices begin at 1; `|` and `/` in genotype fields retain their standard phasing meanings. VCF `POS` is **1-based**. All submitted output should preserve original record IDs and original ALT indices.

**`phenotypes.tsv`**: `sample_id` identifies an independent biological accession associated with one genotype. `assay_repeat` represents one pigment assay measurement. `visual_class` is `pale` or `green`. All accessions belong to a single diploid species.

**`gene_catalog.tsv`**: `primary_transcript_id` denotes the dominant expressed isoform; `secondary_transcript_id` may be blank. `primary_isoform_fraction` is an experimental estimate of usage of the primary isoform in this simulated scenario.

**Historical variant confidence rule:** Use only **`FILTER=PASS`**, genomic REF matching FASTA, and accession genotype **`DP >= 10` plus `GQ >= 20`** for high-confidence genetic burden assessment. Lower-confidence records still require annotation and QC entries. Without functional validation, sequence-based predictions and genotype–phenotype co-segregation must **not** be equated with confirmed biological causality.
