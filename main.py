from logger import log_action
def origin():
    work = True
    while work:
        print('Выбирите нужное действие')
        print('1. Создание первого массива 1d из случайных чисел')
        print('2. Создание второго массива 1d из случайных чисел')
        print('3. Сумма элементов двух массивов и запись в третий массив')
        print('4. Выход')
        num = input()
        count = 0
        if num == "1":
            from create_array import create_array_1d
            lst1 = create_array_1d()
            count += 1
            print(log_action("Создание первого массива 1d из случайных чисел"))
        if num == "2":
            from create_array import create_array_1d
            lst2 = create_array_1d()
            count += 1
            print(log_action("Создание второго массива 1d из случайных чисел"))
        if num == "3" and count == 2:
            from array_lib import sum_arr
            lst3 = sum_arr(lst1,lst2)
            count = 0
            print(log_action("суммирование элементов двух массивов"))       
        if num == "4":
            work = False