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

# проверка интервокальных кластеров 1: встречаются ли они все в интервокале или нет
def M_5():
    #f_2 = ('russian_lexemes.tsv')
    #f_2 = ('russian_wordforms.tsv')
    #f_2 = ('macedonian_lexemes.tsv')
    f_2 = ('polish_wordforms.tsv')

    f3aq_name = 'intervocalic_all_quality_' + f_2
    f3am_name = 'intervocalic_all_manner_' + f_2
    f3mq_name = 'intervocalic_monosyllabic_quality_' + f_2
    f3mm_name = 'intervocalic_monosyllabic_manner_' + f_2

    # поменять имя
    f_name = ('bt_ipa_lexemes_russian.tsv')
    # f_name = ('bt_ipa_wordforms_russian.tsv')
    #f_name = ('bt_ipa_lexemes_macedonian.tsv')
    # f_name = ('bt_ipa_wordforms_polish.tsv')

    f_1 = open(f_name)
    f_1_lines = f_1.readlines()
    f_1.close()
    f_1_lines = f_1_lines[1:]

    man_words = ''
    qua_words = ''

    #man_words = []
    #qua_words = []

    for line in f_1_lines:
        line_bt = re.sub('\n', '', line)
        line_bt = line_bt.split('\t')

        man_word = str(line_bt[3]).strip()
        qua_word = str(line_bt[6]).strip()
        #print(qua_word)

        man_words = man_words + '; ' + man_word
        qua_words = qua_words + ';' + qua_word

        #man_words.append(line_bt[3])
        #qua_words.append(line_bt[6])
    #print(man_words)


    # интервокальные все качество

    f3aq = open(f3aq_name)
    f3aq = f3aq.readlines()
    f3aq = f3aq[1:]
    #print(f3aq)

    f3aq_out_name = 'excess_' + f3aq_name
    f3aq_out = open(f3aq_out_name, 'w')
    f3aq_out.write('excess_clusters_intervocalic_all_quality' + '\n')

    for element in f3aq:
        element = re.sub('\n', '', element)
        #print('the element:', element)
        #for i in range(0, len(qua_words)):
        if element not in qua_words:
            #print(element)
            f3aq_out.write(element + '\n')

    f3aq_out.close()


    # интервокальные все способ
    f3am = open(f3am_name)
    f3am = f3am.readlines()
    f3am = f3am[1:]

    f3am_out_name = 'excess_' + f3am_name
    f3am_out = open(f3am_out_name, 'w')
    f3am_out.write('excess_clusters_intervocalic_all_manner' + '\n')

    for elemen in f3am:
        elemen = re.sub('\n', '', elemen)
        if elemen not in man_words:
            #print(elemen)
            f3am_out.write(elemen + '\n')

    f3am_out.close()


    # интервокальные односложные качество
    f3mq = open(f3mq_name)
    f3mq = f3mq.readlines()
    f3mq = f3mq[1:]

    f3mq_out_name = 'excess_' + f3mq_name
    f3mq_out = open(f3mq_out_name, 'w')
    f3mq_out.write('excess_clusters_intervocalic_monosyllabic_quality' + '\n')

    for eleme in f3mq:
        eleme = re.sub('\n', '', eleme)
        if eleme not in qua_words:
            #print(eleme)
            f3mq_out.write(eleme + '\n')

    f3mq_out.close()


    # интервокальные односложные способ
    f3mm = open(f3mm_name)
    f3mm = f3mm.readlines()
    f3mm = f3mm[1:]

    f3mm_out_name = 'excess_' + f3mm_name
    f3mm_out = open(f3mm_out_name, 'w')
    f3mm_out.write('excess_clusters_intervocalic_monosyllabic_manner' + '\n')
    #print(f3mm)
    #print(man_words)

    for elem in f3mm:
        elem = re.sub('\n', '', elem)
        #print(elem)
        if elem not in man_words:
            #print(elem)
            f3mm_out.write(elem + '\n')

    f3mm_out.close()



# проверка интервокальных кластеров 2: все ли интервокалы они описывают
def M_6():
    #f_2 = ('russian_lexemes.tsv')
    #f_2 = ('russian_wordforms.tsv')
    #f_2 = ('macedonian_lexemes.tsv')
    f_2 = ('polish_wordforms.tsv')

    n_f3aq_name = 'intervocalic_all_quality_' + f_2
    n_f3am_name = 'intervocalic_all_manner_' + f_2
    n_f3mq_name = 'intervocalic_monosyllabic_quality_' + f_2
    n_f3mm_name = 'intervocalic_monosyllabic_manner_' + f_2

    # поменять имя
    #f_name = ('bt_ipa_lexemes_russian.tsv')
    #f_name = ('bt_ipa_wordforms_russian.tsv')
    #f_name = ('bt_ipa_lexemes_macedonian.tsv')
    f_name = ('bt_ipa_wordforms_polish.tsv')

    f_1 = open(f_name)
    f_1_lines = f_1.readlines()
    f_1.close()
    f_1_lines = f_1_lines[1:]


    int_q_full = []
    int_m_full = []


    for line in f_1_lines:
        line_bt = re.sub('\n', '', line)
        line_bt = line_bt.split('\t')

        man_word = str(line_bt[3]).strip()
        qua_word = str(line_bt[6]).strip()
        # print(qua_word)

        man_word_sp = man_word.split('V')
        #print(man_word_sp)
        for element in man_word_sp:
            if element != '':
                if element != '-':
                    if element not in int_m_full:
                        int_m_full.append(element)

        qua_word_sp = qua_word.split('V')
        #print(qua_word_sp)
        for elemen in qua_word_sp:
            if elemen != '':
                if elemen != '-':
                    if elemen not in int_q_full:
                        int_q_full.append(elemen)
                        #print(elemen)


    #print(int_m_full)
    #print(int_q_full)

    int_q_int = []
    int_m_int = []

    fileformreal = open(('presented_manner_clusters_in_' + f_2), 'w')
    fileformreal.write('presented_intervocalic_manner_clusters' + '\n')

    fileforqreal = open(('presented_quality_clusters_in_' + f_2), 'w')
    fileforqreal.write('presented_intervocalic_quality_clusters' + '\n')

    for eleme in int_m_full:
        interv_cl_m = re.search('-([ORLNJ-]+)-', eleme)
        if interv_cl_m:
            #print(interv_cl_m.group(1))
            if interv_cl_m.group(1) not in int_m_int:
                int_m_int.append(interv_cl_m.group(1))
                fileformreal.write(interv_cl_m.group(1) + '\n')

    for elem in int_q_full:
        interv_cl_q = re.search('-([OS-]+)-', elem)
        if interv_cl_q:
            #print(interv_cl_q.group(1))
            if interv_cl_q.group(1) not in int_q_int:
                int_q_int.append(interv_cl_q.group(1))
                fileforqreal.write(interv_cl_q.group((1)) + '\n')

    fileformreal.close()
    fileforqreal.close()

    #print(int_m_int)
    #print(int_q_int)

    # все слова: качество
    nf3aq = open(n_f3aq_name)
    nf3aq = nf3aq.readlines()
    nf3aq = nf3aq[1:]
    #print(nf3aq)

    nf3aq_list = []
    for ele in nf3aq:
        ele = re.sub('\n', '', ele)
        nf3aq_list.append(ele)
    #print(nf3aq_list)

    n_f3aq_out_name = 'not_predicted_' + n_f3aq_name
    nf3aq_out = open(n_f3aq_out_name, 'w')
    nf3aq_out.write('not_predicted_intervocalic_all_quality' + '\n')

    np_aq = []
    for eaq in int_q_int:
        if eaq not in nf3aq_list:
            print(eaq)
            np_aq.append(eaq)
            nf3aq_out.write(eaq + '\n')

    nf3aq_out.close()

    # односложные: качество
    nf3mq = open(n_f3mq_name)
    nf3mq = nf3mq.readlines()
    nf3mq = nf3mq[1:]
    # print(nf3aq)

    nf3mq_list = []
    for el in nf3mq:
        el = re.sub('\n', '', el)
        nf3mq_list.append(el)
    # print(nf3aq_list)

    n_f3mq_out_name = 'not_predicted_' + n_f3mq_name
    nf3mq_out = open(n_f3mq_out_name, 'w')
    nf3mq_out.write('not_predicted_intervocalic_monosyllabic_quality' + '\n')

    np_mq = []
    for emq in int_q_int:
        if emq not in nf3mq_list:
            print(emq)
            np_mq.append(emq)
            nf3mq_out.write(emq + '\n')

    nf3mq_out.close()

    # все слова: способ
    nf3am = open(n_f3am_name)
    nf3am = nf3am.readlines()
    nf3am = nf3am[1:]
    #print(nf3aq)

    nf3am_list = []
    for eles in nf3am:
        eles = re.sub('\n', '', eles)
        nf3am_list.append(eles)
    #print(nf3aq_list)

    n_f3am_out_name = 'not_predicted_' + n_f3am_name
    nf3am_out = open(n_f3am_out_name, 'w')
    nf3am_out.write('not_predicted_intervocalic_all_manner' + '\n')

    np_am = []
    for eam in int_m_int:
        if eam not in nf3am_list:
            print(eam)
            np_am.append(eam)
            nf3am_out.write(eam + '\n')

    nf3am_out.close()

    # односложные: способ
    nf3mm = open(n_f3mm_name)
    nf3mm = nf3mm.readlines()
    nf3mm = nf3mm[1:]
    # print(nf3aq)

    nf3mm_list = []
    for els in nf3mm:
        els = re.sub('\n', '', els)
        nf3mm_list.append(els)
    # print(nf3aq_list)

    n_f3mm_out_name = 'not_predicted_' + n_f3mm_name
    nf3mm_out = open(n_f3mm_out_name, 'w')
    nf3mm_out.write('not_predicted_intervocalic_monosyllabic_manner' + '\n')

    np_mm = []
    for emm in int_m_int:
        if emm not in nf3mm_list:
            print(emm)
            np_mm.append(emm)
            nf3mm_out.write(emm + '\n')

    nf3mm_out.close()



#M_1()
#M_2()
#M_3()
#M_4()
#M_5()
M_6()


print("--- %s seconds ---" % (time.time() - start_time))
