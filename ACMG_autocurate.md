# ACMG_autocurate: classification of variants based on other analyses
This annotator, ACMG Autocurat, is a freely accessible classifier of variants and can classify variants as Pathogenic, Benign, or VUS (variant of unknown significance). The rules used to classify are derived from the 2015 Standards and guidelines for the interpretation of sequence variants via the American College of Medical Genetics and Genomics (ACMG) and the Association for Molecular Pathology AMP).

ACMG_autocurate uses the gnomAD, ClinVar, and SpliceAI annotators, following the logic below, sequentially:

(1) ClinVar: if clinical significance is "Benign" or "Likely benign", classification is Benign. If clinical significance is "Pathogenic" or 
"Likely pathogenic," classification is Pathogenic.

(2) gnomAD: if global_af > .05 (allele is common), then the classification is Benign, as the variant appears many times and is not impactful.

(3) SpliceAI: if all four splice scores are less than .5, classification is Benign.

(4) LOF: if variant is a known LOF variant, classification is variant
