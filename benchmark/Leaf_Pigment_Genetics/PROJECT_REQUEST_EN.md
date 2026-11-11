# Pale-leaf phenotype: sequence and genetic-evidence review of candidate loci

*English translation of the original `PROJECT_REQUEST.md`. Informational only; the original Chinese source was used for the historical comparison.*

## Background and objective

We have assembled a collection of leaf pigment measurements, candidate genomic segments, CDS annotations, and population variant calls for a diploid model plant. Some accessions have relatively pale leaves. Without conducting new experiments, the research team would like to determine which candidate locus is best supported by the available genetic evidence, which variants have credible predicted functional consequences, and the strength of the resulting biological claim.

Please independently choose and implement a suitable analysis workflow. **Prioritize biological inference and data-processing correctness**; figures need only be clear and readable. No external database downloads or large machine learning models are needed. **Do not choose the top locus solely from its functional description**; use sequence evidence, quality evidence, and genotype–phenotype segregation jointly.

## Supplied data

The `data/` folder contains:

- `draft_reference.fa`: reference DNA sequence for candidate regions across scaffolds;
- `genes.gff3`: gene, transcript, and CDS annotations;
- `gene_catalog.tsv`: gene function descriptions and transcript usage information;
- `cohort_variants.vcf`: variants and genotypes for all accessions;
- `phenotypes.tsv`: pigment index and leaf color measurements.

These files represent **small, internally assembled candidate-region records**, not a complete genome-wide scan or a functional validation experiment. Analyze the supplied data as-is.

## Required deliverables

Produce a standalone, reproducible analysis program that:

1. Checks VCF records and genotype quality, retaining explicit QC decisions;
2. Combines FASTA and GFF3 to predict each variant's consequence on relevant transcripts;
3. Integrates accession genotypes and leaf color measurements to evaluate candidate loci;
4. Identifies the best candidate for further functional validation, its supporting variants, and the inference limits;
5. Supplies one figure summarizing key segregation evidence and a concise interpretation.

The team's data-integration system requires **exactly the filenames, table columns, and JSON keys specified in `RESULT_FORMAT.md`**. Numeric outputs must be calculated by code; no hand-filled constants as answers.

The program must provide a `run.sh` accepting two positional arguments:

```bash
bash run.sh /path/to/data /path/to/output
```

The program must dynamically read input paths, all accession IDs, gene IDs, transcript IDs, and variant IDs. **Do not hard-code any of these IDs.** R, Python, or both may be used. Write every result to the requested output folder. Before completion, check whether the code can regenerate its output from the original input.
