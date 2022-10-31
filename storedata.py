import scrapper
import json
import csv

def store_data_as_json():
    scrapper.run_scrapper_bot()
    data = scrapper.stock_info
    with open('scrapped_data/data.json', 'w') as filepath_1:
        json.dump(data, filepath_1)

#store_data_as_json()

def store_data_as_csv():
    scrapper.run_scrapper_bot()
    data = scrapper.stock_info
    with open('scrapped_data/mycsvfile.csv', 'w') as filepath_2:
        csv_data= csv.DictWriter(filepath_2, data.keys())
        csv_data.writeheader()
        csv_data.writerow(data)

store_data_as_csv()