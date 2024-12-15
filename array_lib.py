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

def mean_1d(array: list) -> float:
    mean = 0
    for i in range(len(array)):
        mean += array[i]
    mean \= len(array)
    return mean

def max_1d(array: list) -> float:
    max = array[0]
    for i in range(1,len(array)):
        if max < array[i]:
            max = array[i]
    return max

def min_1d(array: list) -> float:
    min = array[0]
    for i in range(1,len(array)):
        if min > array[i]:
            min = array[i]
    return min

def sum_2d(matrix: list) -> float:
    summ = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i]))
            summ += matrix[i][j]
    return summ

def multi_2d(matrix: list) -> float:
    multi = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i]))
            multi *= matrix[i][j]
    return multi