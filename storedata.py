import json
import csv

def store_data_as_json(data_info):
    with open('scrapped_data/data_info.json', 'w') as filepath_1:
        json.dump(data_info, filepath_1)

def store_data_as_csv(data_info):
    with open('scrapped_data/data_info.csv', 'w') as filepath_2:
        csv_data= csv.DictWriter(filepath_2, data_info.keys())
        csv_data.writeheader()
        csv_data.writerow(data_info)

