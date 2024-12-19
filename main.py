from logger import log_action
def origin():
    work = True
    while work:
        print('Выбирите нужное действие')
        print('4. Выход')
        num = input()
        if num == "4":
            work = False