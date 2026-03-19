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