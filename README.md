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
*transcriber_macedonian .py* transcribes macedonian words from *words_macedonian .txt* to *words_macedonian_IPA .txt*. 

Words are presented as sound-sound-... . 

#### transposer_macedonian .py 
*transposer_macedonian .py* transposes macedonian transcribed words to the expected type to *ipa_lexemes_macedonian .tsv*


#### transpose_russian .py 
*transpose_russian .py* transposes russian words from 
- *lexemes_russian .tsv* to *ipa_lexemes_russian .tsv* 
- *wordforms_russian .tsv* to *ipa_wordforms_russian .tsv*

Words are presented as sound_quality-sound_quality-... . 

Groups of elements: 
- simple vowels: *а*, *о*, *у*, *э*, *ы* 
- hard immutable consonants: *ж*, *ш*, *ц* 
- soft immutable consonants: *щ*, *ч* 
- mutable obstruent consonants: *п*, *б*, *т*, *д*, *к*, *г*, *ф*, *с*, *з*, *х* 
- mutable sonorant consonants: *м*, *н*, *л*, *р* 
- "jot"-vowels: *я*, *ё*, *ю*, *е*

The rules order: 
- all "simple" vowels to > ***V*** 
- hard immutable consonants to > ***O*** 
- soft immutable consonants > ***O*** 
- every other obstruent sconsonants to > ***O*** 
- all sonorants to > R L N 
  - trill/ flap to ***R***
  - lateral approximant to ***L*** 
  - nasal stops to ***N*** 
- jot to > ***J*** 
    - IN ALL POSITIONS *(fricative vs approximant)* 
- *и* to > ***I*** 
- *в* to > ***W*** 
    - IN ALL POSITIONS *(fricative vs approximant)* 
- "jot-"vowels: 
  - following obstruents to > ***V*** 
  - following *ъ* to > ***J-V*** 
  - following *ь* to > ***J-V***
  - following vowel to > ***V-J-V*** 
  - and then: all jot-vowels left to > ***V*** 
- all other *ь* left > 'ø' 



### programs_2 
#### analysis_ 1.py 
*analysis_1 .py* creates: 
- lists of monosyllabic words for each language: 
  - *monosyllabic_russian_lexemes .tsv* and *monosyllabic_russian_wordforms .tsv* for Russian 
  - *monosyllabic_macedonian_lexemes .tsv* 
  - *monosyllabic_polish_wordforms .tsv* 
- lists of absolute onsets and codas of monosyllabic words: 
  - *lists*
- lists of absolute onsets and codas of all words: 
  - *lists*
- tables: word | number of syllables | onset | coda 
  - *tables* 
- tables of absolute onsets and codas and nubmer of its appearance: sequence | frequency (=number of appearance) 
  - *frequency_(type)_(language)_(type of words) .tsv*







