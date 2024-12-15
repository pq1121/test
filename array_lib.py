def sum_1d(array: list) -> float:
    summ = 0
    for i in range(len(array)):
        summ += array[i]
    return summ

def multi_1d(array: list) -> float:
    multi = 1
    for i in range(len(array)):
        multi *= array[i]
    return multi