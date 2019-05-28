# ?кстати что насчёт слов-графических-исключений: marznąć — прописать отдельно?
# ? что делать с носовыми — добавлять ли вставку носового?
# ? что с заимствованиями?
#
#

import pandas as pd
import time
start_time = time.time()


# разбиение на символы: на входе слово, на выходе оно в разделённом виде
def F_lettering(word):
    lettering = ''

    for element in word:
        lettering = lettering + '-' + element
    lettering = lettering.replace('-', '', 1)

    return lettering

# ещё один костыль
def F_2(lexeme):
    #for elem in df['lexemes']:
    elem_1 = lexeme.replace('-', '_')
    elem_low = elem_1.lower()
    # print(elem_low)
    elem_let = F_lettering(elem_low)
    # print(elem_let)
    elem_ipa = F_tr(elem_let)

    #print(elem_ipa)
    return elem_ipa

# тут должно транскрибироваться; на вход разбитое по символам слово
def F_tr(word):
    #print('собственно транскрибация')
    digr = ['sz', 'cz', 'ch', ['rz'], ['dz', 'dź', 'dż']]
    # сначала диграфы,
    # потом C-i

    immut_obstr = ['p', 'b', 't', 'd', 'k', 'g', 'f', 'w', 'h', 'ż', 'ź', 'ś', 'ć', 's', 'c', 'z', 'v', 'q'] # — перед -i это всё меняется просто в себя

    immut_sonorant = ['l', 'ł', 'm', 'n', 'ń', 'r']
    ipa_immut_sonorant = ['L', 'L', 'N', 'N', 'N', 'R']

    simple_voc = ['a', 'o', 'ó', 'u', 'e', 'y', 'ű', 'ö', 'ä', 'â', 'ü', 'ë', 'é', 'è', 'í', 'í', 'á', 'å']
    # что качается носовых, возможно появление носового элемента
    nasal_voc = ['ą', 'ę']

    voc = 'V'
    obstr = 'O'
    jot = 'J'

    #print(word)

    if 'q-u-e' in word:
        word = word.replace('q-u-e', obstr)

    if 'q-u' in word:
        word = word.replace('q-u', (obstr + '-' + obstr))

    if 'c-h' in word:
        word = word.replace('c-h', obstr)

    if 's-z' in word:
        word = word.replace('s-z', obstr)

    if 'c-z' in word:
        word = word.replace('c-z', obstr)

    if 'd-ż' in word:
        word = word.replace('d-ż', obstr)

    if 'd-ź' in word:
        word = word.replace('d-ź', obstr)

    if 'd-z' in word:
        word = word.replace('d-z', obstr)

    if 'r-z' in word:
        word = word.replace('r-z', obstr)

    if 'x' in word:
        word = word.replace('x', (obstr + '-' + obstr))

    if 'j' in word:
        word = word.replace('j', jot)

    # все гласные
    for element in simple_voc:
        if element in word:
            word = word.replace(element, voc)

    # здесь: про носовые
    for elemen in nasal_voc:
        if elemen in word:
            word = word.replace(elemen, voc)

    # здесь все шумные
    for eleme in immut_obstr:
        if eleme in word:
            word = word.replace(eleme, obstr)

    # здесь сонорные все
    for i in range (0, len(immut_sonorant)):
        if immut_sonorant[i] in word:
            word = word.replace(immut_sonorant[i], ipa_immut_sonorant[i])

    # осталось только i
    if 'i-V' in word:
        word = word.replace('i-V', voc)

    if 'i' in word:
        word = word.replace('i', voc)

    #print(word)
    return word


# main function
def M_1():

    #f_name = 'prep_lexemes_polish.tsv'
    f_name = 'wordforms_polish.tsv'
    f2_name = 'ipa_' + f_name

    #df = pd.read_csv(f_name, sep='\t', usecols=['lexemes'])
    df = pd.read_csv(f_name, sep='\t', usecols=['wordform'])

    #df = pd.read_csv(f_name, sep='\t', usecols=['lexemes'], nrows = 7707)
    #df = pd.read_csv(f_name, sep='\t', usecols=['wordform'], nrows = 817)

    df_2 = pd.DataFrame(columns = ['ipa_polish']) # — бесполезная строка по идее

    #df['lexemes'] = df['lexemes'].apply(F_2)
    df['wordform'] = df['wordform'].apply(F_2)

    #df = df.rename(columns = {'lexemes': 'ipa_polish'})
    df = df.rename(columns={'wordform': 'ipa_polish'})

    df.to_csv(f2_name, columns=['ipa_polish'], sep='\t', encoding='utf-8', index=False)


# убирает бессложные слова
def M_2():

    f = open('ipa_wordforms_polish.tsv')
    f_l = f.readlines()

    #f_norm = open('ipa_wordforms_polish.tsv', 'w')
    #f_norm.write('ipa_polish' + '\n')

    for line in f_l:
        if 'V' not in line:
            #f_norm.write(line)
            print(line)

    #f_norm.close()


#M_1()

M_2()

print("--- %s seconds ---" % (time.time() - start_time))
