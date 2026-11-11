# Technical references and design lineage

The following sources informed **error categories and file-format semantics**.
The benchmark's synthetic genomes, genotypes, data positions, synthetic truth,
and sample identifiers were generated for BIPT; they were **not copied from
real cases in the linked repositories**.

1. **SAMtools / hts-specs — VCF v4.3 specification.** Allele index semantics,
   phased (`|`) vs unphased (`/`) genotype separators, and multiallelic records.
   <https://github.com/samtools/hts-specs/blob/master/VCFv4.3.tex>
2. **bcftools documentation.** Reference allele verification, multiallelic
   splitting, indel normalization, and filtering.
   <https://github.com/samtools/bcftools/blob/develop/doc/bcftools.1>
3. **Sequence Ontology GFF3 specification.** 1-based closed interval
   coordinates, strand orientation, and CDS phase conventions.
   <https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md>
4. **European Nucleotide Archive — GFF3 annotation guidance.** Practical CDS
   phase and coordinate definitions.
   <https://ena-docs.readthedocs.io/en/latest/submit/gff3.html>
5. **Ensembl VEP GitHub issue tracker.** Real-world transcript consequence
   annotation implementation discussions and edge cases.
   <https://github.com/Ensembl/ensembl-vep/issues>
6. **Biopython `SeqFeature`.** Features and compound genomic locations,
   especially strand-aware multi-part annotations.
   <https://github.com/biopython/biopython/blob/master/Bio/SeqFeature.py>

**Interpretive caution:** These references document technical failure modes,
not quantitative evidence that any specific AI model often makes those errors.
That claim would require a representative error-frequency study, which BIPT v1.0
is not.
