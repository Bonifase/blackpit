import os
import csv
from django.conf import settings

def get_records(file_name):
    file =  open(settings.BASE_DIR / file_name)
    csvreader = csv.reader(file)
    data = header = []
    header = next(csvreader)
    rows = []
    for row in csvreader:
            rows.append(row)
    file.close()
    for row in rows:
            row_data = dict()
            for index, record in enumerate(row):
                    row_data[header[index]] = record
            data.append(row_data)
    return data

def get_vaccinated():
        records = get_records(settings.VACCINATED_POPULATION)
        return records
