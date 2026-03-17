import csv
from pathlib import Path

def load_csv(path):
    try:
        with open(path, 'r', encoding='utf-8', newline = '') as csv_datei:
            reader = csv.reader(csv_datei)
            data = list(reader)
            return data
    except FileNotFoundError:  
        return "ERROR - FILE NOT FOUND"
    