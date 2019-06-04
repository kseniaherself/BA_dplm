import pandas as pd
import re
import operator

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

# основная функция дл ятаблицы
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

# печатает последние строчки
def M_2():

    #f = open('bt_ipa_lexemes_russian.tsv')
    #f = open('bt_ipa_wordforms_russian.tsv')
    #f = open('bt_ipa_lexemes_macedonian.tsv')
    f = open('bt_ipa_wordforms_polish.tsv')

    f_lines = f.readlines()
    f.close()
    #print(f_lines[-1])
    print(f_lines[7967210])

# запись в словарь
def F_w_d(my_dict, my_key):
    if my_key not in my_dict:
        my_dict[my_key] = 1
    else:
        my_dict[my_key] += 1

    return my_dict

# запись в файл
def F_write_in_file(data , f_name):
    f = open(f_name, 'w')
    f.write(data)
    #print(data)
    f.close()

# сортирует словарь и пишет файл
def F_sort_wd_items(my_items, items_name, items_freq):
    sorted_items = sorted(my_items.items(), key=operator.itemgetter(1), reverse=True)
    #items_freq = items_name + '\t' + 'frequency'

    for k in sorted_items:
        items_freq = items_freq + '\n' + k[0] + '\t' + str(k[1])
    f_name = 'frequency_' + items_name # + '.tsv'
    F_write_in_file(items_freq, f_name)

# списки и частотности
def M_3():

    # ПОМЕНЯТЬ ИМЯ
    #f_name = ('bt_ipa_lexemes_russian.tsv')
    #f_name = ('bt_ipa_wordforms_russian.tsv')
    f_name = ('bt_ipa_lexemes_macedonian.tsv')
    #f_name = ('bt_ipa_wordforms_polish.tsv')

    f_1 = open(f_name)
    f_1_lines = f_1.readlines()
    f_1_lines = f_1_lines[1:]

    # ПОМЕНЯТЬ ИМЯ
    #f_2 = ('russian_lexemes.tsv')
    #f_2 = ('russian_wordforms.tsv')
    f_2 = ('macedonian_lexemes.tsv')
    #f_2 = ('polish_wordforms.tsv')

    mono = 'monosyllabic_'
    al = 'all_'
    qual = 'quality_'       # сонорный—шумный
    man = 'manner_'         # разделение сонорных
    ons = 'onsets_'
    cos = 'codas_'
    freq = 'frequency_'

    f_name_2_mono_qua_ons = mono + qual + ons + f_2
    f_name_2_mono_qua_cos = mono + qual + cos + f_2

    f_name_2_mono_man_ons = mono + man + ons + f_2
    f_name_2_mono_man_cos = mono + man + cos + f_2

    f_name_2_all_qua_ons = al + qual + ons + f_2
    f_name_2_all_qua_cos = al + qual + cos + f_2

    f_name_2_all_man_ons = al + man + ons + f_2
    f_name_2_all_man_cos = al + man + cos + f_2


    f_name_2_mono_qua_ons_fr = freq + mono + qual + ons + f_2
    f_name_2_mono_qua_cos_fr = freq + mono + qual + cos + f_2

    f_name_2_mono_man_ons_fr = freq + mono + man + ons + f_2
    f_name_2_mono_man_cos_fr = freq + mono + man + cos + f_2

    f_name_2_all_qua_ons_fr = freq + al + qual + ons + f_2
    f_name_2_all_qua_cos_fr = freq + al + qual + cos + f_2

    f_name_2_all_man_ons_fr = freq + al + man + ons + f_2
    f_name_2_all_man_cos_fr = freq + al + man + cos + f_2


    onset_qua_mono = [] # инициали простого представления monosyl
    onset_man_mono = [] # инициали дроьного представления monosyl
    coda_qua_mono = []
    coda_man_mono = []

    onset_qua_all = []  # инициали простого представления всех
    onset_man_all = []  # инициали дроьного представления всех
    coda_qua_all = []
    coda_man_all = []


    onset_qua_mono_fr = {}  # инициали простого представления monosyl
    onset_man_mono_fr = {}  # инициали дробного представления monosyl
    coda_qua_mono_fr = {}
    coda_man_mono_fr = {}

    onset_qua_all_fr = {}  # инициали простого представления всех
    onset_man_all_fr = {}  # инициали дробного представления всех
    coda_qua_all_fr = {}
    coda_man_all_fr = {}


    f_2_all_qua_ons = open(f_name_2_all_qua_ons, 'w')
    f_2_all_qua_ons.write('quality_all_onsets' + '\n')

    f_2_all_qua_cos = open(f_name_2_all_qua_cos, 'w')
    f_2_all_qua_cos.write('quality_all_codas' + '\n')

    f_2_all_man_ons = open(f_name_2_all_man_ons, 'w')
    f_2_all_man_ons.write('manner_all_onsets' + '\n')

    f_2_all_man_cos = open(f_name_2_all_man_cos, 'w')
    f_2_all_man_cos.write('manner_all_codas' + '\n')


    f_2_mono_qua_ons = open(f_name_2_mono_qua_ons, 'w')
    f_2_mono_qua_ons.write('quality_monosyllabic_onsets' + '\n')

    f_2_mono_qua_cos = open(f_name_2_mono_qua_cos, 'w')
    f_2_mono_qua_cos.write('quality_monosyllabic_codas' + '\n')

    f_2_mono_man_ons = open(f_name_2_mono_man_ons, 'w')
    f_2_mono_man_ons.write('manner_monosyllabic_onsets' + '\n')

    f_2_mono_man_cos = open(f_name_2_mono_man_cos, 'w')
    f_2_mono_man_cos.write('manner_monosyllabic_codas' + '\n')


    for line in f_1_lines:
        line = re.sub('\n', '', line)
        line = line.split('\t')

        n_s = line[2] # количество слогов
        #print(n_s)

        on_man = line[4] # onset manner
        co_man = line[5] # coda manner

        on_qua = line[7] # onset quality
        co_qua = line[8] # coda quality

        if on_qua not in onset_qua_all:
            onset_qua_all.append(on_qua)
            f_2_all_qua_ons.write(on_qua + '\n')

        if on_man not in onset_man_all:
            onset_man_all.append(on_man)
            f_2_all_man_ons.write(on_man + '\n')

        if co_qua not in coda_qua_all:
            coda_qua_all.append(co_qua)
            f_2_all_qua_cos.write(co_qua + '\n')

        if co_man not in coda_man_all:
            coda_man_all.append(co_man)
            f_2_all_man_cos.write(co_man + '\n')


        onset_qua_all_fr = F_w_d(onset_qua_all_fr, line[7])
        onset_man_all_fr = F_w_d(onset_man_all_fr, line[4])
        coda_qua_all_fr = F_w_d(coda_qua_all_fr, line[8])
        coda_man_all_fr = F_w_d(coda_man_all_fr, line[5])

        #print(co_man)
        #print(n_s)
        if int(n_s) == 1:
            #print(n_s)

            if on_qua not in onset_qua_mono:
                onset_qua_mono.append(on_qua)
                f_2_mono_qua_ons.write(on_qua + '\n')

            if on_man not in onset_man_mono:
                onset_man_mono.append(on_man)
                f_2_mono_man_ons.write(on_man + '\n')

            if co_qua not in coda_qua_mono:
                coda_qua_mono.append(co_qua)
                f_2_mono_qua_cos.write(co_qua + '\n')

            #print(co_man)
            if co_man not in coda_man_mono:
                #print(co_man)
                coda_man_mono.append(co_man)
                f_2_mono_man_cos.write(co_man + '\n')

            onset_qua_mono_fr = F_w_d(onset_qua_mono_fr, line[7])  # инициали простого представления monosyl
            onset_man_mono_fr = F_w_d(onset_man_mono_fr, line[4])  # инициали дробного представления monosyl

            coda_qua_mono_fr = F_w_d(coda_qua_mono_fr, line[8])
            coda_man_mono_fr = F_w_d(coda_man_mono_fr, line[5])


    F_sort_wd_items(onset_qua_mono_fr, f_name_2_mono_qua_ons, 'frequency_quality_monosyllabic_onsets')
    F_sort_wd_items(coda_qua_mono_fr, f_name_2_mono_qua_cos, 'frequency_quality_monosyllabic_codas')

    F_sort_wd_items(onset_man_mono_fr, f_name_2_mono_man_ons, 'frequency_manner_monosyllabic_onsets')
    F_sort_wd_items(coda_man_mono_fr, f_name_2_mono_man_cos, 'frequency_manner_monosyllabic_codas')


    F_sort_wd_items(onset_qua_all_fr, f_name_2_all_qua_ons, 'frequency_quality_all_onsets')
    F_sort_wd_items(coda_qua_all_fr, f_name_2_all_qua_cos, 'frequency_quality_all_codas')

    F_sort_wd_items(onset_man_all_fr, f_name_2_all_man_ons, 'frequency_manner_all_onsets')
    F_sort_wd_items(coda_man_all_fr, f_name_2_all_man_cos, 'frequency_manner_all_codas')

    f_2_all_qua_ons.close()
    f_2_all_qua_cos.close()
    f_2_all_man_ons.close()
    f_2_all_man_cos.close()
    f_2_mono_qua_ons.close()
    f_2_mono_qua_cos.close()
    f_2_mono_man_ons.close()
    f_2_mono_man_cos.close()

# делает списки потенциальных интервокальных кластеров
def M_4():
    #f_2 = ('russian_lexemes.tsv')
    #f_2 = ('russian_wordforms.tsv')
    #f_2 = ('macedonian_lexemes.tsv')
    f_2 = ('polish_wordforms.tsv')

    mono = 'monosyllabic_'
    al = 'all_'
    qual = 'quality_'  # сонорный—шумный
    man = 'manner_'  # разделение сонорных
    ons = 'onsets_'
    cos = 'codas_'
    freq = 'frequency_'

    f_name_2_mono_qua_ons = mono + qual + ons + f_2
    f_name_2_mono_qua_cos = mono + qual + cos + f_2

    f_name_2_mono_man_ons = mono + man + ons + f_2
    f_name_2_mono_man_cos = mono + man + cos + f_2

    f_name_2_all_qua_ons = al + qual + ons + f_2
    f_name_2_all_qua_cos = al + qual + cos + f_2

    f_name_2_all_man_ons = al + man + ons + f_2
    f_name_2_all_man_cos = al + man + cos + f_2


    f_2_all_qua_ons = open(f_name_2_all_qua_ons)
    f2aqo = f_2_all_qua_ons.readlines()
    f2aqo = f2aqo[1:]

    f_2_all_qua_cos = open(f_name_2_all_qua_cos)
    f2aqc = f_2_all_qua_cos.readlines()
    f2aqc = f2aqc[1:]


    f_2_all_man_ons = open(f_name_2_all_man_ons)
    f2amo = f_2_all_man_ons.readlines()
    f2amo = f2amo[1:]

    f_2_all_man_cos = open(f_name_2_all_man_cos)
    f2amc = f_2_all_man_cos.readlines()
    f2amc =f2amc[1:]


    f_2_mono_qua_ons = open(f_name_2_mono_qua_ons)
    f2mqo = f_2_mono_qua_ons.readlines()
    f2mqo = f2mqo[1:]

    f_2_mono_qua_cos = open(f_name_2_mono_qua_cos)
    f2mqc = f_2_mono_qua_cos.readlines()
    f2mqc = f2mqc[1:]


    f_2_mono_man_ons = open(f_name_2_mono_man_ons)
    f2mmo = f_2_mono_man_ons.readlines()
    f2mmo = f2mmo[1:]

    f_2_mono_man_cos = open(f_name_2_mono_man_cos)
    f2mmc = f_2_mono_man_cos.readlines()
    f2mmc = f2mmc[1:]

    f_2_all_qua_ons.close()
    f_2_all_qua_cos.close()
    f_2_all_man_ons.close()
    f_2_all_man_cos.close()
    f_2_mono_qua_ons.close()
    f_2_mono_qua_cos.close()
    f_2_mono_man_ons.close()
    f_2_mono_man_cos.close()

    seqs_1 = []
    seqs_2 = []
    seqs_3 = []
    seqs_4 = []

    # КАЧЕСТВО ВСЕ
    f3aq_name = 'intervocalic_all_quality_' + f_2
    f_3_all_qua = open(f3aq_name, 'w')
    f_3_all_qua.write('intervocalic_all_quality' + '\n')

    for element_c in f2aqc:
        element_c = element_c.replace('\n', '')

        for element_o in f2aqo:
            element_o = element_o.replace('\n', '')

            seq_1 = element_c + '-' + element_o
            seq_1 = seq_1.replace('V-', '')
            seq_1 = seq_1.replace('-V', '')
            seq_1 = seq_1.replace('V', '')

            if seq_1 not in seqs_1:
                if seq_1 != '':
                    f_3_all_qua.write(seq_1 + '\n')
                    seqs_1.append(seq_1)

    # СПОСОБ ВСЕ
    f3am_name = 'intervocalic_all_manner_' + f_2
    f_3_all_man = open(f3am_name, 'w')
    f_3_all_man.write('intervocalic_all_manner' + '\n')

    for elemen_c in f2amc:
        elemen_c = elemen_c.replace('\n', '')

        for elemen_o in f2amo:
            elemen_o = elemen_o.replace('\n', '')

            seq_2 = elemen_c + '-' + elemen_o
            seq_2 = seq_2.replace('V-', '')
            seq_2 = seq_2.replace('-V', '')
            seq_2 = seq_2.replace('V', '')

            if seq_2 not in seqs_2:
                if seq_2 != '':
                    f_3_all_man.write(seq_2 + '\n')
                    seqs_2.append(seq_2)

    # КАЧЕСТВО ОДНОСЛОЖНЫЕ
    f3mq_name = 'intervocalic_monosyllabic_quality_' + f_2
    f_3_mono_qua = open(f3mq_name, 'w')
    f_3_mono_qua.write('intervocalic_monosyllabic_quality' + '\n')

    for eleme_c in f2mqc:
        eleme_c = eleme_c.replace('\n', '')

        for eleme_o in f2mqo:
            eleme_o = eleme_o.replace('\n', '')

            seq_3 = eleme_c + '-' + eleme_o
            seq_3 = seq_3.replace('V-', '')
            seq_3 = seq_3.replace('-V', '')
            seq_3 = seq_3.replace('V', '')

            if seq_3 not in seqs_3:
                if seq_3 != '':
                    f_3_mono_qua.write(seq_3 + '\n')
                    seqs_3.append(seq_3)

    # СПОСОБ ОДНОСЛОЖНЫЕ
    f3mm_name = 'intervocalic_monosyllabic_manner_' + f_2
    f_3_mono_man = open(f3mm_name, 'w')
    f_3_mono_man.write('intervocalic_monosyllabic_manner' + '\n')

    for elem_c in f2mmc:
        elem_c = elem_c.replace('\n', '')

        for elem_o in f2mmo:
            elem_o = elem_o.replace('\n', '')

            seq_4 = elem_c + '-' + elem_o
            seq_4 = seq_4.replace('V-', '')
            seq_4 = seq_4.replace('-V', '')
            seq_4 = seq_4.replace('V', '')

            if seq_4 not in seqs_4:
                if seq_4 != '':
                    f_3_mono_man.write(seq_4 + '\n')
                    seqs_4.append(seq_4)


    f_3_all_qua.close()
    f_3_all_man.close()
    f_3_mono_qua.close()
    f_3_mono_man.close()

# проверка интервокальных клстеров
def M_5():
    

#M_1()
#M_2()
#M_3()
#M_4()
M_5()


print("--- %s seconds ---" % (time.time() - start_time))
