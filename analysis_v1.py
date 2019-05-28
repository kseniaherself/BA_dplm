# monosyl inits
# monosyl fins

import re
import operator
import time
start_time = time.time()

# перевод всего в O-S
def M_0():
    #f = open('ipa_lexemes_russian.tsv')
    f = open('ipa_wordforms_russian.tsv')
    #f = open('ipa_lexemes_macedonian.tsv')
    #f = open('ipa_wordforms_polish.tsv')

    f_lines = f.readlines()
    f_lines = f_lines[1:]

    #f_norm = open('qual_ipa_lexemes_russian.tsv', 'w')
    f_norm = open('qual_ipa_wordforms_russian.tsv', 'w')
    #f_norm = open('qual_ipa_lexemes_macedonian.tsv', 'w')
    #f_norm = open('qual_ipa_wordforms_polish.tsv', 'w')

    #f_norm.write('quality_russian_lexemes' + '\n')
    f_norm.write('quality_russian_wordforms' + '\n')
    #f_norm.write('quality_macedonian_lexemes' + '\n')
    #f_norm.write('quality_polish_wordforms' + '\n')

    son = 'S'
    obs = 'O'

    for line in f_lines:
        for elem in line:
            if elem == 'R':
                line = line.replace('R', son)
            if elem == 'N':
                line = line.replace('N', son)
            if elem == 'J':
                line = line.replace('J', son)
            if elem == 'L':
                line = line.replace('L', son)
            if elem == 'W':
                print(line)
                #line = line.replace('W', obs)

        f_norm.write(line)

    f_norm.close()

# делает списки односложных слов
def M_1():

    #f = open('ipa_lexemes_russian.tsv')
    f = open('ipa_wordforms_russian.tsv')
    #f = open('ipa_lexemes_macedonian.tsv')
    #f = open('ipa_wordforms_polish.tsv')

    #f = open('qual_ipa_lexemes_russian.tsv')
    #f = open('qual_ipa_wordforms_russian.tsv')
    #f = open('qual_ipa_lexemes_macedonian.tsv')
    #f = open('qual_ipa_wordforms_polish.tsv')

    f_lines = f.readlines()
    f_lines = f_lines[1:]

    #f_norm = open('monosyllabic_russian_lexemes.tsv', 'w')
    f_norm = open('monosyllabic_russian_wordforms.tsv', 'w')
    #f_norm = open('monosyllabic_macedonian_lexemes.tsv', 'w')
    #f_norm = open('monosyllabic_polish_wordforms.tsv', 'w')

    #f_norm.write('monosyllabic_russian_lexemes' + '\n')
    f_norm.write('monosyllabic_russian_wordforms' + '\n')
    #f_norm.write('monosyllabic_macedonian_lexemes' + '\n')
    #f_norm.write('monosyllabic_polish_wordforms' + '\n')


    #f_norm = open('qual_monosyllabic_russian_lexemes.tsv', 'w')
    #f_norm = open('qual_monosyllabic_russian_wordforms.tsv', 'w')
    #f_norm = open('qual_monosyllabic_macedonian_lexemes.tsv', 'w')
    #f_norm = open('qual_monosyllabic_polish_wordforms.tsv', 'w')

    #f_norm.write('quality_monosyllabic_russian_lexemes' + '\n')
    #f_norm.write('quality_monosyllabic_russian_wordforms' + '\n')
    #f_norm.write('quality_monosyllabic_macedonian_lexemes' + '\n')
    #f_norm.write('quality_monosyllabic_polish_wordforms' + '\n')

    for line in f_lines:
        i = 0
        for elem in line:
            if elem == 'V':
                i += 1
        if i == 1:
            f_norm.write(line)


        #if 'V' not in line:
        #    # f_norm.write(line)
        #    print(line)

    f_norm.close()

# делат списки сейчас решим чего — инициалей и финалей односложных слов
def M_2():
    #f = open('monosyllabic_russian_lexemes.tsv')
    #f = open('monosyllabic_russian_wordforms.tsv')
    #f = open('monosyllabic_macedonian_lexemes.tsv')
    #f = open('monosyllabic_polish_wordforms.tsv')

    #f = open('qual_monosyllabic_russian_lexemes.tsv')
    #f = open('qual_monosyllabic_russian_wordforms.tsv')
    #f = open('qual_monosyllabic_macedonian_lexemes.tsv')
    f = open('qual_monosyllabic_polish_wordforms.tsv')

    f_lines = f.readlines()
    f_lines = f_lines[1:]  # РАБОЧАЯ ВЕРСИЯ ДЛЯ ВСЕХ СЛОВ


    #f_init = open('monosyllabic_onsets_russian_lexemes.tsv', 'w')
    #f_init.write('monosyllabic_onsets_russian_lexemes' + '\n')

    #f_fin = open('monosyllabic_codas_russian_lexemes.tsv', 'w')
    #f_fin.write('monosyllabic_codas_russian_lexemes' + '\n')


    #f_init = open('monosyllabic_onsets_russian_wordforms.tsv', 'w')
    #f_init.write('monosyllabic_onsets_russian_wordforms' + '\n')

    #f_fin = open('monosyllabic_codas_russian_wordforms.tsv', 'w')
    #f_fin.write('monosyllabic_codas_russian_wordforms' + '\n')


    #f_init = open('monosyllabic_onsets_macedonian_lexemes.tsv', 'w')
    #f_init.write('monosyllabic_onsets_macedonian_lexemes' + '\n')

    #f_fin = open('monosyllabic_codas_macedonian_lexemes.tsv', 'w')
    #f_fin.write('monosyllabic_codas_macedonian_lexemes' + '\n')


    #f_init = open('monosyllabic_onsets_polish_wordforms.tsv', 'w')
    #f_init.write('monosyllabic_onsets_polish_wordforms' + '\n')

    #f_fin = open('monosyllabic_codas_polish_wordforms.tsv', 'w')
    #f_fin.write('monosyllabic_codas_polish_wordforms' + '\n')


    # ПУСТАЯ СТРОКА

    #f_init = open('qual_monosyllabic_onsets_russian_lexemes.tsv', 'w')
    #f_init.write('quality_monosyllabic_onsets_russian_lexemes' + '\n')

    #f_fin = open('qual_monosyllabic_codas_russian_lexemes.tsv', 'w')
    #f_fin.write('quality_monosyllabic_codas_russian_lexemes' + '\n')


    #f_init = open('qual_monosyllabic_onsets_russian_wordforms.tsv', 'w')
    #f_init.write('quality_monosyllabic_onsets_russian_wordforms' + '\n')

    #f_fin = open('qual_monosyllabic_codas_russian_wordforms.tsv', 'w')
    #f_fin.write('quality_monosyllabic_codas_russian_wordforms' + '\n')


    #f_init = open('qual_monosyllabic_onsets_macedonian_lexemes.tsv', 'w')
    #f_init.write('quality_monosyllabic_onsets_macedonian_lexemes' + '\n')

    #f_fin = open('qual_monosyllabic_codas_macedonian_lexemes.tsv', 'w')
    #f_fin.write('quality_monosyllabic_codas_macedonian_lexemes' + '\n')


    f_init = open('qual_monosyllabic_onsets_polish_wordforms.tsv', 'w')
    f_init.write('quality_monosyllabic_onsets_polish_wordforms' + '\n')

    f_fin = open('qual_monosyllabic_codas_polish_wordforms.tsv', 'w')
    f_fin.write('quality_monosyllabic_codas_polish_wordforms' + '\n')


    onset = 'V'
    coda = 'V'

    initials = []
    finals = []

    for line in f_lines:
        res_init = re.match('([^V]+?)(((-)*?[V])|$)', line)
        if res_init:
            onset = res_init.group(1)

        if onset not in initials:
            initials.append(onset)

            f_init.write(onset + '\n')

        res_fin = re.match('[V]*?-([^V]+?$)', line)
        if res_fin:
            coda = res_fin.group(1)

        if coda not in finals:
            finals.append(coda)

            f_fin.write(coda + '\n')

    f_init.close()
    f_fin.close()

# делает списки инициалей и финалей всех слов — потому что если вдруг для македонского будет мало, я возьму отсюда
def M_3():
    #f = open('ipa_lexemes_russian.tsv')
    #f = open('ipa_wordforms_russian.tsv')
    #f = open('ipa_lexemes_macedonian.tsv')
    #f = open('ipa_wordforms_polish.tsv')

    #f = open('qual_ipa_lexemes_russian.tsv')
    #f = open('qual_ipa_wordforms_russian.tsv')
    #f = open('qual_ipa_lexemes_macedonian.tsv')
    f = open('qual_ipa_wordforms_polish.tsv')

    f_lines = f.readlines()
    f_lines = f_lines[1:]  # РАБОЧАЯ ВЕРСИЯ ДЛЯ ВСЕХ СЛОВ

    #f_init = open('all_onsets_russian_lexemes.tsv', 'w')
    #f_init.write('all_onsets_russian_lexemes' + '\n')

    #f_fin = open('all_codas_russian_lexemes.tsv', 'w')
    #f_fin.write('all_codas_russian_lexemes' + '\n')


    #f_init = open('all_onsets_russian_wordforms.tsv', 'w')
    #f_init.write('all_onsets_russian_wordforms' + '\n')

    #f_fin = open('all_codas_russian_wordforms.tsv', 'w')
    #f_fin.write('all_codas_russian_wordforms' + '\n')


    #f_init = open('all_onsets_macedonian_lexemes.tsv', 'w')
    #f_init.write('all_onsets_macedonian_lexemes' + '\n')

    #f_fin = open('all_codas_macedonian_lexemes.tsv', 'w')
    #f_fin.write('all_codas_macedonian_lexemes' + '\n')


    #f_init = open('all_onsets_polish_wordforms.tsv', 'w')
    #f_init.write('all_onsets_polish_wordforms' + '\n')

    #f_fin = open('all_codas_polish_wordforms.tsv', 'w')
    #f_fin.write('all_codas_polish_wordforms' + '\n')


    # ПУСТАЯ СТРОКА

    #f_init = open('qual_all_onsets_russian_lexemes.tsv', 'w')
    #f_init.write('quality_all_onsets_russian_lexemes' + '\n')

    #f_fin = open('qual_all_codas_russian_lexemes.tsv', 'w')
    #f_fin.write('quality_all_codas_russian_lexemes' + '\n')


    #f_init = open('qual_all_onsets_russian_wordforms.tsv', 'w')
    #f_init.write('quality_all_onsets_russian_wordforms' + '\n')

    #f_fin = open('qual_all_codas_russian_wordforms.tsv', 'w')
    #f_fin.write('quality_all_codas_russian_wordforms' + '\n')


    #f_init = open('qual_all_onsets_macedonian_lexemes.tsv', 'w')
    #f_init.write('quality_all_onsets_macedonian_lexemes' + '\n')

    #f_fin = open('qual_all_codas_macedonian_lexemes.tsv', 'w')
    #f_fin.write('quality_all_codas_macedonian_lexemes' + '\n')


    f_init = open('qual_all_onsets_polish_wordforms.tsv', 'w')
    f_init.write('quality_all_onsets_polish_wordforms' + '\n')

    f_fin = open('qual_all_codas_polish_wordforms.tsv', 'w')
    f_fin.write('quality_all_codas_polish_wordforms' + '\n')


    onset = 'V'
    coda = 'V'

    initials = []
    finals = []

    for line in f_lines:
        res_init = re.match('([^V]+?)(((-)*?[V])|$)', line)
        if res_init:
            onset = res_init.group(1)

        if onset not in initials:
            initials.append(onset)

            f_init.write(onset + '\n')

        res_fin = re.match('[V]*?-([^V]+?$)', line)
        if res_fin:
            coda = res_fin.group(1)

        if coda not in finals:
            finals.append(coda)

            f_fin.write(coda + '\n')

    f_init.close()
    f_fin.close()

    return initials, finals

# делает таблицу общую
def M_4():
    #f = open('ipa_lexemes_russian.tsv')
    #f = open('ipa_wordforms_russian.tsv')
    #f = open('ipa_lexemes_macedonian.tsv')
    f = open('ipa_wordforms_polish.tsv')

    f_lines = f.readlines()
    f_lines = f_lines[1:]  # РАБОЧАЯ ВЕРСИЯ ДЛЯ ВСЕХ СЛОВ

    #f_bt = open('bt_lexemes_russian.tsv', 'w')
    #f_bt.write('lexeme_russian' + '\t' + 'number_syllables' + '\t' + 'onset' + '\t' + 'coda' + '\n')

    #f_bt = open('bt_wordforms_russian.tsv', 'w')
    #f_bt.write('wordforms_russian' + '\t' + 'number_syllables' + '\t' + 'onset' + '\t' + 'coda' + '\n')

    #f_bt = open('bt_lexemes_macedonian.tsv', 'w')
    #f_bt.write('lexeme_macedonian' + '\t' + 'number_syllables' + '\t' + 'onset' + '\t' + 'coda' + '\n')

    f_bt = open('bt_wordforms_polish.tsv', 'w')
    f_bt.write('wordforms_polish' + '\t' + 'number_syllables' + '\t' + 'onset' + '\t' + 'coda' + '\n')

    initials = []
    finals = []

    for line in f_lines:
        i= 0
        onset = 'V'
        coda = 'V'

        #print(line)
        #res_init = re.match('([^V]+?)(((-)*?[V])|$)', line)
        res_init = re.search('^([^V]+?)(((-)*?[V])|$)', line)
        if res_init:
            onset = res_init.group(1)

        if onset not in initials:
            initials.append(onset)

            #print(line, 'это было слово', onset)

        #print(line)
        res_fin = re.search('[V]*?-([^V]+?$)', line)
        if res_fin:
            coda = res_fin.group(1)

        if coda not in finals:
            finals.append(coda)

            #print(coda)

        for elem in line:
            if elem == 'V':
                i += 1

        word = line.strip()
        word = re.sub('\n', '', word)
        #print('word: ', word)

        f_bt.write(word + '\t' + str(i) + '\t' + onset + '\t' + coda + '\n')

    f_bt.close()

    # теперь посчитаем частотность

# добавляет в таблицу качество
def M_5():
    f_o = open('lexemes_russian.tsv')
    #f_o = open('wordforms_russian.tsv')
    #f_o = open('lexemes_macedonian.tsv')
    #f_o = open('wordforms_polish.tsv')

    f_o_lines = f_o.readlines()
    f_o_lines = f_o_lines[1:]

    lines_o = [] # СЛОВА В ОРФОГРАФИИ
    for line_o in f_o_lines:
        line_o = re.sub('\n', '', line_o)
        #line_o = line_o.split('\t')
        lines_o.append(line_o)



    f_bt = open('bt_lexemes_russian.tsv') # РАБОЧАЯ ТАБЛИЦА
    #f_bt = open('bt_wordforms_russian.tsv')
    #f_bt = open('bt_lexemes_macedonian.tsv')
    #f_bt = open('bt_wordforms_polish.tsv')


    f_bt_lines = f_bt.readlines()
    f_bt_lines = f_bt_lines[1:]

    lines_bt = []
    for line_bt in f_bt_lines:
        line_bt = re.sub('\n', '', line_bt)
        line_bt = line_bt.split('\t')
        lines_bt.append(line_bt)


    # таблицы куда всё записывается
    f_bt = open('big_table_lexemes_russian.tsv', 'w')
    f_bt.write('lexeme_russian' + '\t' + 'number_syllables' + '\t' + 'lexeme_q1' + '\t' + 'onset_q1' + '\t' + 'coda_q1'
               + '\t' + 'lexeme_q2' + '\t' + 'onset_q2' + '\t' + 'coda_q2' + '\n')

    # f_bt = open('big_table_wordforms_russian.tsv', 'w')
    # f_bt.write('wordforms_russian' + '\t' + 'number_syllables' + '\t' + 'onset' + '\t' + 'coda' + '\n')

    # f_bt = open('big_table_lexemes_macedonian.tsv', 'w')
    # f_bt.write('lexeme_macedonian' + '\t' + 'number_syllables' + '\t' + 'onset' + '\t' + 'coda' + '\n')

    #f_bt = open('big_table_wordforms_polish.tsv', 'w')
    #f_bt.write('wordforms_polish' + '\t' + 'number_syllables' + '\t' + 'onset' + '\t' + 'coda' + '\n')


    f_q = open('qual_ipa_lexemes_russian.tsv')
    # f_q = open('qual_ipa_wordforms_russian.tsv')
    # f_q = open('qual_ipa_lexemes_macedonian.tsv')
    # f_q = open('qual_ipa_wordforms_polish.tsv')

    f_q_lines = f_q.readlines()
    f_q_lines = f_q_lines[1:]  # РАБОЧАЯ ВЕРСИЯ ДЛЯ ВСЕХ СЛОВ

    lines_f_q = []
    for line_fq in f_q_lines:
        line_fq = re.sub('\n', '', line_fq)
        line_fq = line_fq.split('\t')
        lines_f_q.append(line_fq)


    for i in range(0, len(lines_bt)):
        line_q = str(lines_f_q[i])
        #print(line_q)
    #for line_q in f_q_lines:
        #line_q = re.sub('\n', '', line_q)
        #line_q = line_q.split('\t')
        line_q = line_q.replace('[', '')
        line_q = line_q.replace(']', '')
        line_q = line_q.replace("'", "")


        onset = 'V'
        coda = 'V'

        # print(line)
        # res_init = re.match('([^V]+?)(((-)*?[V])|$)', line)
        res_init = re.search('^([^V]+?)(((-)*?[V])|$)', line_q)
        if res_init:
            onset = res_init.group(1)

        # print(line)
        res_fin = re.search('[V]*?-([^V]+?$)', line_q)
        if res_fin:
            coda = res_fin.group(1)

        word = lines_o[i]
        f_bt.write(str(word) + '\t' + str(lines_bt[i][1]) + '\t' + str(lines_bt[i][0]) + '\t' + str(lines_bt[i][2])
                   + '\t' + str(lines_bt[i][3]) + '\t' + str(line_q) + '\t' + str(onset) + '\t' + str(coda) + '\n')

    f_q.close()

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
def F_sort_wd_items(my_items, items_name):
    sorted_items = sorted(my_items.items(), key=operator.itemgetter(1), reverse=True)
    items_freq = items_name + '\t' + 'frequency'
    for k in sorted_items:
        items_freq = items_freq + '\n' + k[0] + '\t' + str(k[1])
    f_name = 'frequency_' + items_name + '.tsv'
    F_write_in_file(items_freq, f_name)

# частотность последовательностей
def M_6():

    onsets_list = []
    finals_list = []

    onsets_dict = {}
    codas_dict = {}

    #f_tt = open('bt_lexemes_russian.tsv')
    #f_tt = open('bt_wordforms_russian.tsv')
    #f_tt = open('bt_lexemes_macedonian.tsv')
    f_tt = open('bt_wordforms_polish.tsv')

    f_lis = f_tt.readlines()
    f_lis = f_lis[1:]
    #print(f_lis)

    for line in f_lis:
        line = re.sub('\n', '', line)
        line = line.split('\t')

        #print(line)

        onsets_list.append(line[2])
        finals_list.append(line[3])

        onsets_dict = F_w_d(onsets_dict, line[2])
        codas_dict = F_w_d(codas_dict, line[3])

    #print(onsets_dict)
    #print(codas_dict)

    #F_sort_wd_items(onsets_dict, 'onset_russian_lexemes')
    #F_sort_wd_items(codas_dict, 'coda_russian_lexemes')

    #F_sort_wd_items(onsets_dict, 'onset_russian_wordforms')
    #F_sort_wd_items(codas_dict, 'coda_russian_wordforms')

    #F_sort_wd_items(onsets_dict, 'onset_macedonian_lexemes')
    #F_sort_wd_items(codas_dict, 'coda_macedonian_lexemes')

    F_sort_wd_items(onsets_dict, 'onset_polish_wordforms')
    F_sort_wd_items(codas_dict, 'coda_polish_wordforms')

# должна считать вероятность и сравнивать
def M_7():
    f_name = ('frequency_onset_russian_lexemes.tsv')
    # f_name = ('frequency_coda_russian_lexemes.tsv')

    # f_name = ('frequency_onset_russian_wordforms.tsv')
    # f_name = ('frequency_coda_russian_wordforms.tsv')

    # f_name = ('frequency_onset_macedonian_lexemes.tsv')
    # f_name = ('frequency_coda_macedonian_lexemes.tsv')

    # f_name = ('frequency_onset_polish_wordforms.tsv')
    # f_name = ('frequency_coda_polish_wordforms.tsv')

    f = open(f_name)
    f_lines = f.readlines()
    f_lines = f_lines[1:]

    total_app = 0
    lines = []

    for line in f_lines:
        line = re.sub('\n', '', line)
        line = line.split('\t')
        lines.append(line)
        total_app = total_app + int(line[1])

    print(total_app)

    f_name_upd = 'probability_' + f_name
    first_line = f_lines[0]
    first_line = re.sub('\n', '', first_line)

    #f_bt = open(f_name_upd, 'w')
    #f_bt.write(first_line + '\t' + 'probability' + '\n')

    for lin in lines:
        prob = round((int(lin[1]))/total_app, 25)
        print(prob)

# сделаем сбор интервокальных кластеров и проверим их
def M_8():
    f_init = ('monosyllabic_onsets_russian_lexemes.tsv')
    f_fin = ('monosyllabic_codas_russian_lexemes.tsv')

    f_i = open(f_init)
    f_f = open(f_fin)

    f_i_l = f_i.readlines()
    f_f_l = f_f.readlines()

    f_i_l = f_i_l[1:]
    f_f_l = f_f_l[1:]

    intv = []
    for i in range(0, len(f_i_l)):
        for j in range(0, len(f_f_l)):
            print(i+j)





#M_0()

#M_1()

#M_2()

#M_3()

#M_4()

M_5()

#M_6()

#M_7()

#M_8()

print("--- %s seconds ---" % (time.time() - start_time))
