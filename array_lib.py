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
    mean /= len(array)
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
        for j in range(len(matrix[i])):
            summ += matrix[i][j]
    return summ

def multi_2d(matrix: list) -> float:
    multi = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            multi *= matrix[i][j]
    return multi

def mean_2d(matrix: list) -> float:
    mean = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            mean += matrix[i][j]
    mean /= (len(matrix) * len(matrix[0]))
    return mean

def max_2d(matrix: list) -> float:
    max = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if max < matrix[i][j]:
                max = matrix[i][j]
    return max

def min_2d(matrix: list) -> float:
    min = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if min > matrix[i][j]:
                min = matrix[i][j]
    return min

def diff_arr(arr1: list,arr2: list) -> list:
    diff_lst = []
    for i in range(len(arr1)):
        diff_lst.append(int(arr1[i] - arr2[i]))
    return diff_lst