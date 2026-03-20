import builtins

from csv_analyzer.validation import errorHandling
from csv_analyzer.transform import extract_column

def average(table: list, column: int):

    if(errorHandling(table, column, True) != "NO ERROR"):
        return errorHandling(table, column, True)
    
    count = 0
    sum = 0
    columnList = extract_column(table, column)
    for element in columnList:
        sum+=element
        count+=1

    return sum/count

def median(table: list, column : int):

    if(errorHandling(table, column, True) != "NO ERROR"):
        return errorHandling(table, column, True)

    columnList = extract_column(table, column)

    middle = len(columnList) // 2
    columnList.sort()
    if len(columnList) % 2 == 0:
        return (float(columnList[middle - 1]) + float(columnList[middle])) / 2
    else:
        return float(columnList[middle])

def min(table: list, column : int):

    if(errorHandling(table, column, True) != "NO ERROR"):
        return errorHandling(table, column, True)

    columnList = extract_column(table, column)
    minA = columnList[0]
    for element in columnList:
        if element < minA:
            minA = element

    return minA

def max(table: list, column : int):

    if(errorHandling(table, column, True) != "NO ERROR"):
        return errorHandling(table, column, True)

    columnList = extract_column(table, column)
    maxA = columnList[0]
    for element in columnList:
        if element > maxA:
            maxA = element

    return maxA

def count(table: list, column : int):

    if(errorHandling(table, column, False) != "NO ERROR"):
        return errorHandling(table, column, False)

    columnList = extract_column(table, column)
    count = 0
    for element in columnList:
        count+=1

    return count

def sum(table: list, column : int):

    if(errorHandling(table, column, True) != "NO ERROR"):
        return errorHandling(table, column, True)

    columnList = extract_column(table, column)
    sum = 0
    for element in columnList:
        sum+=element

    return sum

def mode(table: list, column : int):

    if(errorHandling(table, column, False) != "NO ERROR"):
        return errorHandling(table, column, False)

    columnList = extract_column(table, column)
    frequency = {}
    for element in columnList:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1

    modeA = None
    max_freq = 0
    for key, value in frequency.items():
        if value > max_freq:
            max_freq = value
            modeA = key

    return modeA

def variance(table: list, column : int):

    if(errorHandling(table, column, True) != "NO ERROR"):
        return errorHandling(table, column, True)

    columnList = extract_column(table, column)
    mean = average(table, column)
    variance = builtins.sum([(x - mean) ** 2 for x in columnList]) / len(columnList)

    return variance

def std_dev(table: list, column : int):

    if(errorHandling(table, column, True) != "NO ERROR"):
        return errorHandling(table, column, True)

    varianceA = variance(table, column)
    std_dev = varianceA ** 0.5

    return std_dev