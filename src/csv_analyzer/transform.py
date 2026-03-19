def extract_column(table, column):  
    count = 0
    columnList = []
    for row in table:
        if count != 0:
            columnList.append(float(row[column]))
        count+=1

    return columnList