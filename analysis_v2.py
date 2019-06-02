import pandas as pd
import re
import time
start_time = time.time()

# считает количесво слогов
def F_1(word):
    i = 0

    for elem in word:
        if elem == 'V':
            i = i + 1

    return i

# ищет инициали
def F_2(word):
    onset = 'V'

    res_init = re.search('^([^V]+?)(((-)*?[V])|$)', word)
    if res_init:
        onset = res_init.group(1)

    return onset

# ищет финали
def F_3(word):
    coda = 'V'

    res_fin = re.search('[V]*?-([^V]+?$)', word)
    if res_fin:
        coda = res_fin.group(1)

    return coda

# меняет на качество
def F_4(word):
    son = 'S'

    word = word.replace('R', son)
    word = word.replace('L', son)
    word = word.replace('N', son)
    word = word.replace('J', son)

    #for element in word:
    #    if element == 'R':
    #        word = word.replace

    return word

# основная функция
def M_1():
    #f_name = ('ipa_lexemes_russian.tsv')
    #f_name = ('ipa_wordforms_russian.tsv')
    #f_name = ('ipa_lexemes_macedonian.tsv')
    f_name = ('ipa_wordforms_polish.tsv')

    f2_name = 'bt_' + f_name

    #df = pd.read_csv(f_name, sep='\t', usecols=['ipa_russian'])
    #df = pd.read_csv(f_name, sep='\t', usecols=['ipa_macedonian'])
    df = pd.read_csv(f_name, sep='\t', usecols=['ipa_polish'])

    # df = pd.read_csv(f_name, sep='\t', usecols=['ipa_russian'], nrows = 7707)
    # df = pd.read_csv(f_name, sep='\t', usecols=['ipa_macedonian'], nrows = 817)
    # df = pd.read_csv(f_name, sep='\t', usecols=['ipa_polish'], nrows = 2384)

    # переименовывает колонки
    #df = df.rename(columns={'ipa_russian': 'word_q1'})
    #df = df.rename(columns = {'ipa_macedonian': 'word_q1'})
    df = df.rename(columns = {'ipa_polish': 'word_q1'})


    #f_name_orth = 'lexemes_russian.tsv'
    #f_name_orth = 'wordforms_russian.tsv'
    #f_name_orth = 'lexemes_macedonian.tsv'
    f_name_orth = 'wordforms_polish.tsv'

    #df_o = pd.read_csv(f_name_orth, sep='\t', usecols=['lexemes'])       # русский
    df_o = pd.read_csv(f_name_orth, sep='\t', usecols=['wordform'])      # русский и польский
    #df_o = pd.read_csv(f_name_orth, sep='\t', usecols=['dict_entry'])    # македонский

    #df_o = df_o.rename(columns={'lexemes': 'word_ortho'})          # русский
    df_o = df_o.rename(columns = {'wordform': 'word_ortho'})       # русский и польский
    #df_o = df_o.rename(columns = {'dict_entry': 'word_ortho'})    # македонский


    df['word_ortho'] = df_o['word_ortho']

    # считает слоги
    df['number_syllables'] = df['word_q1'].apply(F_1)

    # инициали q1
    df['onset_q1'] = df['word_q1'].apply(F_2)

    # финали q1
    df['coda_q1'] = df['word_q1'].apply(F_3)

    # меняет на q2
    df['word_q2'] = df['word_q1'].apply(F_4)

    # инициали q2
    df['onset_q2'] = df['word_q2'].apply(F_2)

    # финали q2
    df['coda_q2'] = df['word_q2'].apply(F_3)


    df.to_csv(f2_name, columns=['word_ortho', 'number_syllables', 'word_q1', 'onset_q1', 'coda_q1', 'word_q2', 'onset_q2', 'coda_q2'], sep='\t', encoding='utf-8')#, index=False)
    #df.to_csv(f2_name, sep='\t', encoding='utf-8') #, index=False)


def M_2():

    #f = open('bt_ipa_lexemes_russian.tsv')
    #f = open('bt_ipa_wordforms_russian.tsv')
    #f = open('bt_ipa_lexemes_macedonian.tsv')
    f = open('bt_ipa_wordforms_polish.tsv')

    f_lines = f.readlines()
    f.close()
    #print(f_lines[-1])
    print(f_lines[7967210])

#M_1()
#M_2() 


print("--- %s seconds ---" % (time.time() - start_time))
