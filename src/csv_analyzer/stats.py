from csv_analyzer import load_csv

def average(table: list, column: int):
    if(not table):
        return "ERROR - EMPTY TABLE"
    if(not isinstance(table,list)):
        return "ERROR - TABLE NEEDS TO BE A LIST"
    if(not isinstance(column, int)):
        return "ERROR - COLUMN NEEDS TO BE A INT"
    if(column>=len(table[0])):
        return "ERROR - COLUMN OUT OF RANGE FOR TABLE"
    try:
        float(table[1][column])
    except(TypeError, ValueError):
        return "ERROR - THE COLUMN IN YOUR TABLE MUST CONTAIN NUMBERS"
    
    count = 0
    sum = 0
    for row in table:
        if count != 0:
            sum += float(row[column])
        count+=1

    return sum/count

