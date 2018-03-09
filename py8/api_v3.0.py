"""
    Author:Arvin Shaffer
    Function:Air Quality Index Calculation
    Version:3.0
    Date:03/9/2018
    2.0 New Function:use json
    3.0 New Function:read json file and write to csv file
"""
import csv
import json

def process_json_file(filepath):
    """
    Parse json file
    :param filepath:
    :return:
    """
    f = open(filepath, mode='r', encoding='utf-8')
    city_list = json.load(f)
    return city_list

def main():
    filepath = input('Please enter the json file path:')
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])

    lines = []

    lines.append(list(city_list[0].keys()))
    for city in city_list:
        lines.append(list(city.values()))

    f = open('aqi.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()

if __name__ == '__main__':
    main()
