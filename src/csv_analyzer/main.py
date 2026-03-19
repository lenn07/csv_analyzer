from csv_analyzer import load_csv
from csv_analyzer import average
from csv_analyzer import median    

path1 = "data/student_performance_prediction_dataset-2.csv"

table = load_csv(path1)

print(average(table=table, column=1))
print(median(table=table, column=0))