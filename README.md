# EHRmappings
mappings between NDC2RXCUI and ICD2PheWas

## Mappings
- all mappings are in resources directory
- all mappings are stored as pickle files
- all mappings are dictionary
- ICD to PheWas
> we have icd9 to phewas; icd10 to phewas; the icd2phewas is the combination of both icd9 and icd10
- NDC to RXCUI
- RXCUI to ingredient level RXCUI
> this mapping can have multiple mapped results (the values in dict are set)
- CPT, ICD10, ICD9 procedure codes to CCS code

## mappings format
- rxcui2name: one to one
- rxcui_remap: one to many; value is a set
- rxcui2ingredient: one to many; value is a set; if value is an empty set then itself is a ingredient
- ndc2rxcui: one to one
- icd2phewas: one to one
- cpt2ccs: one to one


## notebook
- jupyter notebooks for how we map the codes

##  Current version
- current mappings are based on **RxNorm Full Monthly Release October 5, 2020**