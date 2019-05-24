# шумные (O) - носовые (N) - плавные (l, r) (L) - глайды (j, w) (W)
# без разделения шумных

# решить про /в/
# mind гласные но я забыла в контексте чего ...

# ! мягкий и твёрдый знак

# а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ (ъ) ы (ь) э ю я
# просто гласные: а о у э ы
# йотированные: я ё ю е и

# hard immutable: ш ж ц
# soft immutable: щ ч ???й
# hard/soft mutable: п б т д к г ф !в! с з х _ м н _ л _ р
# что делать с й? зависит ведь от ударения
# тоже проблемы с В!

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

# тут должно транскрибироваться; на вход разбитое по символам слово
def F_tr(word):

    hard_immut = ['ш', 'ж', 'ц']
    soft_immut = ['щ', 'ч']
    mutable_obstr = ['п', 'б', 'т', 'д', 'к', 'г', 'ф', 'с', 'з', 'х']

    mutable_sonorant = ['м', 'н', 'л', 'р']
    ipa_mutable_sonorant = ['N', 'N', 'L', 'R']

    hard_voc = ['а', 'о', 'у', 'э', 'ы']
    jot_voc = ['я', 'ё', 'ю', 'е']

    ii = 'I'
    ww = 'W'

    er = 'ъ'
    erj = 'ь'

    voc = 'V'
    obstr = 'O'
    jot = 'J'


    for element in hard_voc:
        if element in word:
            word = word.replace(element, voc)

    for elemen in hard_immut:
        if elemen in word:
            word = word.replace(elemen, obstr)

    for eleme in soft_immut:
        if eleme in word:
            word = word.replace(eleme, obstr)

    for elem in mutable_obstr:
        if elem in word:
            word = word.replace(elem, obstr)

    for i in range (0, len(mutable_sonorant)):
        if mutable_sonorant[i] in word:
            word = word.replace(mutable_sonorant[i], ipa_mutable_sonorant[i])

    if 'й' in word:
        word = word.replace('й', jot)

    if 'и' in word:
        word = word.replace('и', ii)

    if 'в' in word:
        word = word.replace('в', ww)
    # И ПРОПИСАТЬ ПРАВИЛА ДЛЯ В

    for el in jot_voc:

        crutch_1 = obstr + '-' + el
        crutch_2 = obstr + '-' + voc
        if crutch_1 in word:
            word = word.replace(crutch_1, crutch_2)

        crutch_3 = er + '-' + el
        crutch_4 = jot + '-' + voc
        if crutch_3 in word:
            word = word.replace(crutch_3, crutch_4)

        crutch_5 = erj + '-' + el
        crutch_6 = jot + '-' + voc
        if crutch_5 in word:
            word = word.replace(crutch_5, crutch_6)

        crutch_7 = voc + '-' + el
        crutch_8 = voc + '-' + jot + '-' + voc
        if crutch_7 in word:
            word = word.replace(crutch_7, crutch_8)

        if el in word:
            word = word.replace(el, voc)

        if erj in word:
            word = word.replace(('-' + erj), '')

    #print(word)
    return word

# ещё один костыль
def F_2(lexeme):
    #for elem in df['lexemes']:
    elem_1 = lexeme.replace('-', '_')
    elem_low = elem_1.lower()
    # print(elem_low)
    elem_let = F_lettering(elem_low)
    # print(elem_let)
    elem_ipa = F_tr(elem_let)

    return elem_ipa

# main function
def M_1():

    #f_name = 'lexemes_russian.tsv'
    f_name = 'wordforms_russian.tsv'
    f2_name = 'ipa_' + f_name

    #df = pd.read_csv(f_name, sep='\t', usecols=['lexemes'])
    df = pd.read_csv(f_name, sep='\t', usecols=['wordform'])

    #df = pd.read_csv(f_name, sep='\t', usecols=['lexemes'], nrows = 7707)

    df_2 = pd.DataFrame(columns = ['ipa_russian'])

    #df['lexemes'] = df['lexemes'].apply(F_2)
    df['wordform'] = df['wordform'].apply(F_2)

    #df = df.rename(columns = {'lexemes': 'ipa_russian'})
    df = df.rename(columns = {'wordform': 'ipa_russian'})

    df.to_csv(f2_name, columns = ['ipa_russian'], sep='\t', encoding='utf-8', index=False)


def M_2():
    #f = open('ipa_lexemes_russian.tsv')
    f = open('prep_ipa_wordforms_russian.tsv')

    f_l = f.readlines()
    f_l = f_l[1:]

    #f_norm = open('ipa_lexemes_russian.tsv', 'w')
    f_norm = open('ipa_wordforms_russian.tsv', 'w')

    f_norm.write('ipa_russian' + '\n')

    for line in f_l:
        if 'I' in line:
            line = line.replace('I', 'V')

        if '_-' in line:
            line = line.replace('_-', '')

        if 'V' in line:
            f_norm.write(line)
        #    print(line)


    f_norm.close()

#M_1()

M_2()

print("--- %s seconds ---" % (time.time() - start_time))
