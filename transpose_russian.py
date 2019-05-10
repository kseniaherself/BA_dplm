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

import time
start_time = time.time()

def M_1():
    hard_immut = ['ш', 'ж', 'ц']
    ipa_hard_immut = ['O', 'O', 'O']

    soft_immut = ['щ', 'ч']
    ipa_soft_immut = ['O', 'O']

    mutable_obstr = ['п', 'б', 'т', 'д', 'к', 'г', 'ф', 'с', 'з', 'х']
    ipa_mutable_obstr = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']

    mutable_sonorant = ['м', 'н', 'л', 'р']
    ipa_mutable_sonorant = ['N', 'N', 'L', 'R']



M_1()

print("--- %s seconds ---" % (time.time() - start_time))
