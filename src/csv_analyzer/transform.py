def extract_column(table, column):  
    count = 0
    columnList = []
    for row in table:
        if count != 0:
            if(isinstance(row[column], str)):
                columnList.append(row[column])
            else:
                columnList.append(float(row[column]))
        count+=1

    return columnList