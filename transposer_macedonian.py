import pandas as pd
import time
start_time = time.time()

# перевод всего, замена по элементам потому что диграфы
def F_2(word):

    ipa_s = ['j']

    obstr_dgrphs = ['dz', 'ts', 'tʃ', 'dʒ']

    syls = ['R', 'L', 'N']

    son_dgrphs = ['lj', 'nj']

    vows = ['a', 'o', 'u', 'e', 'i', 'è', 'ì', 'ə']

    simple_obstr = ['b', 'v', 'ɡ', 'd', 'ɟ', 'ʒ', 'z', 'k', 'p', 's', 't', 'c', 'f', 'x', 'ʃ']

    simple_sons = ['m']
    ipa_simple_sons = ['N']

    obstr = 'O'
    vow = 'V'

    for elem in obstr_dgrphs:
        if elem in word:
            word = word.replace(elem, obstr)

    for el in syls:
        if el in word:
            word = word.replace(el, ('ə-' + el))

    if 'lj' in word:
        word = word.replace('lj', 'l')

    if 'nj' in word:
        word = word.replace('nj', 'n')

    for elemen in simple_obstr:
        if elemen in word:
            word = word.replace(elemen, obstr)

    for element in vows:
        if element in word:
            word = word.replace(element, vow)

    if 'm' in word:
        word = word.replace('m', 'N')

    word = word.upper()

    #print(word)
    return word

def M_1():

    #f_name = 'lexemes_polish.tsv'
    f_name = 'ipa_ipa_lexemes_macedonian.txt'
    f2_name = 'ipa_lexemes_macedonian.tsv'

    df = pd.read_csv(f_name, sep='\t', usecols=['ipa_macedonian'])

    #df = pd.read_csv(f_name, sep='\t', usecols=['ipa_macedonian'], nrows = 87)

    df_2 = pd.DataFrame(columns = ['ipa_macedonian']) # — бесполезная строка по идее

    #df['lexemes'] = df['lexemes'].apply(F_2)
    df['ipa_macedonian'] = df['ipa_macedonian'].apply(F_2)


    df.to_csv(f2_name, columns=['ipa_macedonian'], sep='\t', encoding='utf-8', index=False)


M_1()

print("--- %s seconds ---" % (time.time() - start_time))
