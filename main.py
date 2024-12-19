from logger import log_action
def origin():
    work = True
    while work:
        print('Выбирите нужное действие')
        print('1. Создание первого массива 1d из случайных чисел')
        print('2. Создание второго массива 1d из случайных чисел')
        print('4. Выход')
        num = input()
        if num == "1":
            from create_array import create_array_1d
            lst1 = create_array_1d()
        if num == "2":
            from create_array import create_array_1d
            lst2 = create_array_1d()
        if num == "4":
            work = False