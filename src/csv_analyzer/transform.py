def extract_column(table, column):  
    count = 0
    columnList = []
    for row in table:
        if count != 0:
            try:
                dataInFloat = float(row[column])
            except ValueError:
                dataInFloat = row[column]
            columnList.append(dataInFloat)
        count+=1

    return columnList

def headerToIndex(table, column):
    count = 0
    if(column.isdigit()):
        return int(column)
    for element in table[0]:
        if element == column:
            return count
        count+=1
    return -1