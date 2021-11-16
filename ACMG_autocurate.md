# ACMG_autocurate: classification of variants based on other analyses
ACMG is a freely accessible classifier of variants, classifying variants as Pathogenic, Benign, or VUS (variant of unknown significance).

ACMG_autocurate uses the gnomAD, ClinVar, and SpliceAI annotators, following the logic below, sequentially:

(1) ClinVar: if clinical significance is "Benign" or "Likely benign", classification is Benign. If clinical significance is "Pathogenic" or 
"Likely pathogenic," classification is Pathogenic.

(2) gnomAD: if global_af > .05 (allele is common), then the classification is Benign, as the variant appears many times and is not impactful.

(3) SpliceAI: if all four splice scores are less than .5, classification is Benign.

(4) LOF: if variant is a known LOF variant, classification is variant