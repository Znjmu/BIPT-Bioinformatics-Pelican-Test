# Limitations, validity, and responsible interpretation

> [!WARNING]
> **This benchmark is a pilot methodological demonstration, not a validated general-purpose AI science index.** Numbers are precise relative to a specific algorithm. Their interpretation is conditional on its scientific assumptions.

## 1. A single narrow task cannot establish general bioinformatics ability

The benchmark covers **one synthetic plant-variant interpretation workflow**. It does not independently test bulk RNA-seq normalization, single-cell integration, spatial transcriptomics, experimental design in large cohorts, proteomics, metagenomics, or bedside diagnostics. Such skills require their own separate benchmark cases.

## 2. The reference truth is generated, not observed experimentally

A synthetic ground truth enables deterministic grading, but the generator's design controls the problem's mechanisms. Real variant data introduce population structure, annotation uncertainty, incomplete phase information, variant calling errors, expression dependence, functional redundancy, and phenotype measurement noise that are not comprehensively represented here.

## 3. Candidate ranking is not necessarily unique

**The most consequential limitation is in held-out instance 1.** The historical scorer's ordering is:

1. More pale accessions with biallelic predicted disruption.
2. Fewer green accessions with such disruption.
3. More pale accessions carrying any disrupted haplotype.

A biologically cautious alternative may prioritize **perfect or cleaner phenotype segregation** instead. Both approaches use real evidence; the exercise did not pre-register a set of alternative admissible candidates. As a result, **8/10 valid models disagreed with the fixed reference gene on that instance**. The margin between the two highest scored models and the rest is therefore **partly a rubric-design effect**, not an unambiguous measure of core biology expertise.

**Proposed fix:** Freeze a multi-objective reference rule or a set of valid candidate outcomes *before* collecting model submissions in future versions.

## 4. Prediction of loss of function is not experimental validation

Counting `stop_gained`, `frameshift`, and `start_lost` changes in primary transcripts is an operational rule. In reality, regulatory variation, protein rescue, alternative isoforms, and the severity of splice defects can matter. An in silico genotype/phenotype association **cannot establish causality**.

## 5. 30-minute limit is not a scored speed dataset

The tasks were designed around a **30-minute wall-clock budget**, but the public artifacts do **not** preserve complete start/finish timestamps or a uniform measurement of compute costs for each model. Consequently, the leaderboard must **not** be used to make claims such as “Model X is faster than Model Y.”

## 6. Model configurations were not standardized

The eleven entries contain different reasoning settings, including Extreme, Ultra-high, Max, High, Default and Light. API versions, third-party routing, prompt truncation, tooling, and token/compute allocations may be different. Model labels came from the submissions, not a provider verification protocol.

## 7. Ceiling effects and limited discrimination

All ten valid submissions earned perfect weighted **13/13 QC**, **23/23 haplotype**, **4/4 replay**, and **3/3 integrity** categories. Several also earned **35/35 annotation**. High scores reduce the benchmark's ability to rank comparably competent systems.

## 8. Figure quality is not objectively graded

The 3 artifact points concern filename, minimum pixel dimension, PNG format, and content/nonempty notes. No human aesthetics rating, content extraction, or independent evidence-to-plot validation was carried out. Thus **the benchmark does not substantiate superiority in research illustration quality**.

## 9. Missing submission is not a measured failure of scientific reasoning

The GPT-5.6 Luna Light archive supplied no analysis deliverable. Its code-path score of 0.00 is a bookkeeping state. Publishing it as **N/A** prevents an invalid interpretation. A complete rerun would be needed to measure scientific performance under that configuration.

## 10. Independence of trials and uncertainty

One submission per configuration was graded. The experiment did not quantify model run-to-run variation and did not include a power analysis or frequentist/Bayesian uncertainty intervals for rankings. A 2-point difference should **not** be assigned a p-value or treated as provider-level scientific superiority.

## 11. Release of hidden cases compromises future blind rounds

The full historical source archive is intended for **retrospective replication**. Publishing it exposes the v1.0 hidden generator and answer conditions, allowing future agents to train on or memorize these exact cases. Reusing v1.0 after disclosure would no longer be an independent blind evaluation.

## 12. Conflicts, independence, and author's views

The BIPT authors control task construction, scorer design, and interpretation. The score is computed by software but reflects those choices. Unless separately disclosed, this repository makes **no claim of third-party independent audit, peer-reviewed endorsement, provider approval, or validated commercial use**.

**Formal disclaimer:** **The results, rankings, observations, and conclusions are the author's views only**; they do not reflect the official position of any AI model company, research institution, scientific journal, or other organization.
