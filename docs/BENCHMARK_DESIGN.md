# BIPT v1.0 — Design rationale and challenge architecture

## 1. Research question

**Can an AI coding agent select scientifically defensible computational analyses, execute them correctly, and avoid biologically invalid conclusions when confronted with interlocking sequence and inheritance edge cases?**

BIPT v1.0 is deliberately narrower than an all-purpose bioinformatics benchmark. It targets **genetic variant interpretation in diploid plant samples**, rather than general coding skill, software trivia, or visual presentation. The study uses **small synthetic datasets** to make the grading oracle deterministic and the per-task computation feasible within an approximately 30-minute end-to-end agent budget.

> [!IMPORTANT]
> A **harder dataset is not necessarily a larger dataset**. The benchmark places ambiguity in the *meaning of the data*—strand orientation, transcript consequence, reference consistency, phased genotype, and segregation—not in file size or the number of cells or variants.

## 2. The public-facing research request

The scenario is a research team's attempt to prioritize candidate loci for a pale-leaf pigment phenotype in a diploid plant, using limited sequence and phenotype evidence. Participants see the five input file types and a fixed output schema. They are **not told the list of planted error conditions**, given an expected ranking, or asked to maximize a benchmark score.

The unmodified historical **Chinese-language** request is preserved in [`benchmark/Leaf_Pigment_Genetics/PROJECT_REQUEST.md`](../benchmark/Leaf_Pigment_Genetics/PROJECT_REQUEST.md). An [English reading translation](../benchmark/Leaf_Pigment_Genetics/README_EN.md) is provided separately and **was not the historical prompt**. The result schema is preserved in [`RESULT_FORMAT.md`](../benchmark/Leaf_Pigment_Genetics/RESULT_FORMAT.md).

### Public released dataset

| Characteristic | Released instance |
|---|---:|
| Candidate genes in `gene_catalog.tsv` | 14 |
| Distinct primary transcript IDs | 14 |
| Genes with a listed secondary transcript | 3 |
| VCF records | 71 |
| Total ALT alleles across VCF records | 72 |
| Independent diploid accessions | 20 |
| Phenotype measurement rows | 40 |
| Reference scaffolds | 2 |

The data are **simulated**, not collected from real plants. A genome reference, gene architecture, variants, phenotype classes, sample identifiers, and technical repeats were built for this evaluation. The released data do not test raw read alignment, sequencing error modeling at instrument level, or a real-world genome-wide association study.

## 3. Biological traps and what they measure

### 3.1 Coordinate semantics

**Problem:** VCF `POS` and GFF3 `start/end` positions use 1-based coordinates. Programming libraries often use 0-based half-open slices. A hidden off-by-one error can convert the wrong codon even while code runs without an exception.

**Evidence expected:** compare VCF REF to the base or interval in FASTA; reconstruct CDS positions using correct coordinate conversions.

### 3.2 Strand-aware coding interpretation

**Problem:** for a minus-strand gene, the genomic REF/ALT allele orientation is not equivalent to the transcript's 5′→3′ coding strand.

**Evidence expected:** reverse-complement and reorder CDS segments according to strand, then translate reference and alternative CDS sequences.

**Failure indication:** a genuine stop-gained variant is mislabeled missense or synonymous, or the reverse effect on a negative-strand transcript.

### 3.3 Transcript specificity and CDS phase

**Problem:** a variant may overlap one isoform's coding sequence but not another's. GFF3 CDS `phase` describes codon offset in the 5′ direction of the transcript rather than arbitrary frame alignment.

**Evidence expected:** record consequence **per ALT, per relevant transcript**, preserve the primary transcript definition when computing high-confidence burden, and distinguish minor-isoform-only effects.

**Failure indication:** any high-impact effect on a minor transcript is automatically assigned to the primary product or the whole gene.

### 3.4 Multiple ALT alleles

**Problem:** VCF records may list two or more alternate alleles; `GT=1|2` means **different ALT alleles on the two haplotypes**, not two copies of ALT 1.

**Evidence expected:** enumerate the per-ALT consequence using `alt_index` and interpret the diploid genotype exactly.

**Failure indication:** multi-allelic alleles are collapsed into one mutation or both haplotypes are deemed disruptive despite only one severe ALT.

### 3.5 Cis/trans haplotype phase

**Problem:** two individually severe mutations can affect **one haplotype (cis)** or **both haplotypes (trans)**. Counting variant rows instead of disrupted haplotypes overstates recessive genetic burden.

**Evidence expected:** aggregate phased ALT calls per haplotype. For example:

```text
Variant A: 0|1
Variant B: 0|1     same ALT-bearing haplotype → 1 disrupted haplotype (cis)

Variant A: 0|1
Variant B: 1|0     opposite ALT-bearing haplotypes → 2 disrupted haplotypes (trans)
```

**Failure indication:** both sets called `biallelic_disruptive=true` merely because two severe variants appear in the same sample.

### 3.6 Reference inconsistency versus site filters

**Problem:** a VCF record may have `FILTER=PASS` but a reference allele that does not match the supplied FASTA at its reported genomic position.

**Evidence expected:** **independent reference sequence check**, not trust in the VCF FILTER alone.

### 3.7 Low-confidence sample genotypes

**Problem:** a visually compelling variant/phenotype match may be explained by low-depth or low-quality genotypes.

**Evidence expected:** for the historical reference solution, a genotype is high confidence when its `DP >= 10`, `GQ >= 20`, and all relevant fields are interpretable; a variant's site also requires REF matching and `FILTER=PASS`. The exact thresholds are *benchmark conventions*, not universal best-practice guidelines.

### 3.8 Pseudoreplication of phenotype repeats

**Problem:** two pigment measurements from one accession do **not** represent two independent biological genotypes.

**Evidence expected:** count samples independently by `sample_id` and distinguish `n_independent_accessions` from `n_phenotype_measurements`.

### 3.9 Misleading biological plausibility

**Problem:** a gene's description may make it look plausibly involved in chloroplast or pigment function, but it can carry the wrong phase configuration or an unconvincing segregation pattern.

**Evidence expected:** combine gene function with genotype QC, primary-transcript consequence, and independent sample segregation. **Functional annotation is supporting context, not automatic causal proof.**

### 3.10 Causal interpretation

**Problem:** in silico predicted loss of function plus case/control cosegregation does **not** confirm a gene's causal effect. Actual functional testing, segregation in additional independent material, complementation, or mechanistic experiments would be needed.

**Evidence expected:** explicitly distinguish **prioritization** from **established causality**.

## 4. Hidden-instance replay

The same program is independently run on:

- **Released instance:** sample identifiers and schema supplied in this repository.
- **Held-out instance 1:** new IDs, sequences/locations, **24 diploid accessions**, and an altered causal-role assignment.
- **Held-out instance 2:** newly generated IDs and biological roles, **16 diploid accessions**.

The two hidden instances are different generated datasets, not simply shuffled rows of the released table. The correct top locus is not a fixed ID and changes with the generator configuration. All three cases share the **same interface and scientific interpretation conventions**.

> [!CAUTION]
> Publishing a completed benchmark's hidden generation code/seed makes that version **unfit for future blinded evaluation**. To keep a new task blind, rotate the generator scenarios and hold out new instances server-side.

## 5. Required outputs and why the schema is fixed

The mandatory outputs are:

1. `variant_consequences.tsv` — one row per `variant_id` × `alt_index` × relevant `transcript_id`.
2. `variant_qc.tsv` — per-record FASTA/VCF consistency and high-confidence carrier count.
3. `accession_gene_burden.tsv` — per accession × gene number of disrupted haplotypes and biallelic flag.
4. `summary.json` — top candidate, transcript, supporting variants, evidence model, accession counts, and causal-claim status.
5. `segregation.png` — a summary chart.
6. `interpretation.md` — a concise interpretation.

A rigid schema is necessary to grade without relying on another LLM. The fields **do not reveal the expected values**.

## 6. Scope and construct validity

What is measured reasonably well:

- Parsing and scientifically interpreting **VCF, GFF3, FASTA, and phenotype tables**.
- Building a data-driven pipeline with multiple dependent steps.
- Generalizing code to hidden records/genes and preventing simple hard-coded answers.
- Avoiding the most immediate inference errors within the simulated plant-genetics scenario.

What is **not** established:

- Performance across all of bioinformatics (single-cell, proteomics, long reads, epigenomics, medical informatics, etc.).
- General causal discovery capability.
- Robustness to noisy real-world genotyping, population structure, or large-scale genome mapping.
- Reliability in clinical use, or individual model providers' advertised capabilities.

Read [Limitations](LIMITATIONS.md) before drawing general conclusions.
