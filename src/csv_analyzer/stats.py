from csv_analyzer import load_csv

def average(table: list, column: int):

    if(errorHandling(table, column) != "NO ERROR"):
        return errorHandling(table, column)
    
    count = 0
    sum = 0
    for row in table:
        if count != 0:
            sum += float(row[column])
        count+=1

    return sum/count

def median(table: list, column : int):

    if(errorHandling(table, column) != "NO ERROR"):
        return errorHandling(table, column)

    count = 0
    columnList = []
    for row in table:
        if count != 0:
            columnList.append(float(row[column]))
        count+=1

    middle = len(columnList) // 2
    columnList.sort()
    if len(columnList) % 2 == 0:
        return (float(columnList[middle - 1]) + float(columnList[middle])) / 2
    else:
        return float(columnList[middle])

def errorHandling(table, column):
    if(not table):
        return "ERROR - EMPTY TABLE"
    if(not isinstance(table,list)):
        return "ERROR - TABLE NEEDS TO BE A LIST"
    if(not isinstance(column, int)):
        return "ERROR - COLUMN NEEDS TO BE A INT"
    if(column>=len(table[0]) or column<0):
        return "ERROR - COLUMN OUT OF RANGE FOR TABLE"
    if(len(table)==1):
        return "ERROR - TABLE HAS NO COLUMNS(WE ASSUME THE FIRST ROW IS A HEADER)"
    
    count = 0
    for row in table:
        if count != 0:
            if(row[column].isnumeric() == False):
                return "ERROR - COLUMN CONTAINS NON NUMERIC VALUES"
        count+=1

    
    return "NO ERROR"
