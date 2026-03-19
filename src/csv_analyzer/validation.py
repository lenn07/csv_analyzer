from csv_analyzer.transform import extract_column

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
    
    columnList = extract_column(table, column)
    for element in columnList:
        if(not isinstance(element, float)):
            return "ERROR - COLUMN CONTAINS NON NUMERIC VALUES"
      
    return "NO ERROR"