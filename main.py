from logger import log_action
def origin():
    count = 0
    work = True
    while work:
        print('Выбирите нужное действие')
        print('1. Создание первого массива 1d из случайных чисел')
        print('2. Создание второго массива 1d из случайных чисел')
        print('3. Сумма элементов двух массивов и запись в третий массив')
        print('4. Вывести массив на экран')
        print('5. Выход')
        num = input()
        if num == "1":
            from create_array import create_array_1d
            lst1 = create_array_1d()
            count += 1
            print(log_action("Создание первого массива 1d из случайных чисел\n"))
        elif num == "2":
            from create_array import create_array_1d
            lst2 = create_array_1d()
            count += 1
            print(log_action("Создание второго массива 1d из случайных чисел\n"))
        elif num == "3" and count == 2:
            from array_lib import sum_arr
            lst3 = sum_arr(lst1,lst2)
            count = 0
            print(log_action("суммирование элементов двух массивов\n"))
        elif num == "4":
            work1 = True
            while work1:
                print('Выбирите нужное действие')
                print('1. Вывести первый массив')
                print('2. Вывести второй массив')
                print('3. Вывести полученный массив')
                print('4. Выход в предыдущее меню\n')
                num1 = input()
                if num1 == "1":
                    print(f'Первый массив {lst1}\n')
                elif num1 == "2":
                    print(f'Первый массив {lst2}\n')
                elif num1 == "3":
                    print(f'Первый массив {lst3}\n')
                elif num1 == "4":
                    work1 = False
                else:
                    print('Не выбран пункт меню!!!')
        elif num == "5":
            work = False
        else:
            print('Не выбран пункт меню!!!')