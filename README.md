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

## notebook
- jupyter notebooks for how we map the codes

##  Current version
- current mappings are based on **RxNorm Full Monthly Release October 5, 2020**