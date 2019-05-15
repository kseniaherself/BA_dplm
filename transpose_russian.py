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
def F_transposer(word):
    #olala

    hard_immut = ['ш', 'ж', 'ц']
    ipa_hard_immut = ['O', 'O', 'O']

    soft_immut = ['щ', 'ч']
    ipa_soft_immut = ['O', 'O']

    mutable_obstr = ['п', 'б', 'т', 'д', 'к', 'г', 'ф', 'с', 'з', 'х']
    ipa_mutable_obstr = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']

    mutable_sonorant = ['м', 'н', 'л', 'р']
    ipa_mutable_sonorant = ['N', 'N', 'L', 'R']

    hard_voc = ['а', 'о', 'у', 'э', 'ы']
    ipa_hard_voc = ['A', 'Ɔ', 'U', 'Ɛ', 'Y']

    jot_voc = ['я', 'ё', 'ю', 'е']
    ipa_jot_voc = ['A', 'Ɔ', 'U', 'E']

    soft_voc = 'и'
    ipa_soft_voc = 'I'

    jot = 'й'
    ipa_jot = 'J'

    er = ['ъ']
    erj = ['ь']

    # печатает слова с оригинальным '-'
    #if '_' in word:
    #    print(word)

    # печатает слова с ъ/ь после hard immutable
    #for a in range (1, 3):
        #if (hard_immut[a] + '-ь') in word:
            #print(word)

    # печатает слова с й перед йотированным гласным
    #for a in range (1, len(jot_voc)):
    #    if ('-й-' + jot_voc[a]) in word:
    #        print(word)

    # use replace не sub !!!!!
    for element in word:

        for n in range(0, (len(hard_voc))):
            if hard_voc[n] == element:
                #print(hard_voc[m])
                word = word.replace(hard_voc[n], ipa_hard_voc[n])
                #print(word)

        for i in range(0, (len(hard_immut))):
            if hard_immut[i] == element:
                word = word.replace(hard_immut[i], ipa_hard_immut[i])

        for j in range(0, (len(soft_immut))):
            if soft_immut[j] == element:
                word = word.replace(soft_immut[j], ipa_soft_immut[j])

    word = word.replace(jot, ipa_jot)
    word = word.replace(soft_voc, ipa_soft_voc)

    for k in range(1, (len(jot_voc))):
        word = word.replace(('O-' + jot_voc[k]), ('O-' + ipa_hard_voc[k]))

    for elem in word:
        for l in range(1, (len(mutable_obstr))):
            if mutable_obstr[l] == elem:
                word = word.replace(mutable_obstr[l], ipa_mutable_obstr[l])

    for m in range(1, (len(jot_voc))):
        word = word.replace(('O-' + jot_voc[m]), ('O-' + ipa_jot_voc[m]))

    print(word)
    for o in range(1, len(jot_voc)):
        for p in range(1, (len(jot_voc))):
            word = word.replace((jot_voc[p] + '-' + jot_voc[o]), (jot_voc[p] + '-' + ipa_jot + '-' + ipa_jot_voc[o]))

        for q in range(1, len(ipa_hard_voc)):
            word = word.replace((ipa_hard_voc[q] + '-' + jot_voc[o]), (ipa_hard_voc[q] + '-' + ipa_jot + '-' + ipa_jot_voc[o]))

        word = word.replace((ipa_soft_voc + '-' + jot_voc[o]), (ipa_soft_voc + '-' + ipa_jot + '-' + ipa_jot_voc[o]))

    #if '' in word:
    #    word = word.replace('', '')

    #for a in range(1, len(jot_voc)):
    #    if ('O-' + jot_voc[a]) in word:
    #        print(word)


    print(word)


def M_1():

    f_name = 'lexemes_russian.tsv'
    #f2_name = 'ipa_' + f_name
    #df = pd.read_csv(f_name, sep='\t', usecols=['lexemes'])
    df = pd.read_csv(f_name, sep='\t', usecols=['lexemes'], nrows = 777)

    for elem in df['lexemes']:
        elem_1 = elem.replace('-', '_')
        elem_low = elem_1.lower()
        #print(elem_low)
        elem_let = F_lettering(elem_low)
        #print(elem_let)
        elem_ipa = 'xz'
        F_transposer(elem_let)




M_1()

print("--- %s seconds ---" % (time.time() - start_time))
