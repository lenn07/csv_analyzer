from csv_analyzer.validation import errorHandling
from csv_analyzer.transform import extract_column

def average(table: list, column: int):

    if(errorHandling(table, column) != "NO ERROR"):
        return errorHandling(table, column)
    
    count = 0
    sum = 0
    columnList = extract_column(table, column)
    for element in columnList:
        sum+=element
        count+=1

    return sum/count

def median(table: list, column : int):

    if(errorHandling(table, column) != "NO ERROR"):
        return errorHandling(table, column)

    columnList = extract_column(table, column)

    middle = len(columnList) // 2
    columnList.sort()
    if len(columnList) % 2 == 0:
        return (float(columnList[middle - 1]) + float(columnList[middle])) / 2
    else:
        return float(columnList[middle])

def min(table: list, column : int):

    if(errorHandling(table, column) != "NO ERROR"):
        return errorHandling(table, column)

    columnList = extract_column(table, column)
    minA = columnList[0]
    for element in columnList:
        if element < minA:
            minA = element

    return minA

def max(table: list, column : int):

    if(errorHandling(table, column) != "NO ERROR"):
        return errorHandling(table, column)

    columnList = extract_column(table, column)
    maxA = columnList[0]
    for element in columnList:
        if element > maxA:
            maxA = element

    return maxA

def count(table: list, column : int):

    if(errorHandling(table, column) != "NO ERROR"):
        return errorHandling(table, column)

    columnList = extract_column(table, column)
    count = 0
    for element in columnList:
        count+=1

    return count

def sum(table: list, column : int):

    if(errorHandling(table, column) != "NO ERROR"):
        return errorHandling(table, column)

    columnList = extract_column(table, column)
    sum = 0
    for element in columnList:
        sum+=element

    return sum