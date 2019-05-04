import pandas as pd
import time
start_time = time.time()

def m_1():
    f_name = 'macedonian_dict1.tsv'
    f2_name = 'words_macedonian.txt'

    df = pd.read_csv(f_name, sep='\t', usecols=['POS', 'dict_entry'])

    df = df.loc[df['POS'] != 'Вид збор: Скратеница']
    df = df.loc[df['POS'] != 'Вид збор: Сложенка']
    df = df.loc[df['POS'] != 'Вид збор: Извик']
    df = df.loc[~df['dict_entry'].str.contains('’')]
    df = df.loc[~df['dict_entry'].str.contains('-')]

    df['dict_entry'] = df['dict_entry'].str.replace('!', '')

    df.to_csv(f2_name, columns = ['dict_entry'], sep='\t', encoding='utf-8', index=False)

m_1()


print("--- %s seconds ---" % (time.time() - start_time))
