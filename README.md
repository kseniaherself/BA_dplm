# dplm
the repository for my BA thesis 

## Structure of the project 
data > [**programs_1**] > transcribed data > [**programs_2**] 

***programs_1*** 

***programs_2***  
which transpone *tr_data* into *O-S.assoc* and outputs frequency distribution of consonants and clusters

## Programms 

### programs_1 
#### macedonian_table_1 .py 
*macedonian_table_1 .py* has as an input pre-prepared file *macedonian_dict1 .tsv* and as an output it produces a file with list of dictionary lexemes in *words_macedonian .txt*. 

The program excludes abbreviations, conjunction, compounds, words including '’' (*д’тка*, *д’такње*), '-' (А-бомба, алфа-честичка). It replaces *!* 

#### transcriber_macedonian .py 
*transcriber_macedonian .py* transcribes macedonian words from *words_macedonian .txt* to *ipa_words_macedonian .txt*. 

Words are presented as sound-sound-... . 

#### transpose_russian .py 
*transpose_russian .py* transposes russian words from *XXX .txt* to *ipa_XXX .txt*. 

Words are presented as sound_quality-sound_quality-... . 




### programs_2 
