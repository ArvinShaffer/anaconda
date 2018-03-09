"""
    Author:Arvin Shaffer
    Function:Air Quality Index Calculation
    Version:4.0
    Date:03/9/2018
    2.0 New Function:use json
    3.0 New Function:read json file and write to csv file
    4.0 New Function:According to the input file to determine whether json or csv, and the corresponding operation
"""
import csv
import json
import os


def process_json_file(filepath):
    """
    Parse json file
    :param filepath:
    :return:
    """
    # f = open(filepath, mode='r', encoding='utf-8')
    # city_list = json.load(f)
    # return city_list
    with open(filepath, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)

def process_csv_file(filepath):
    """
    Parse csv file
    :param filepath:
    :return:
    """
    with open(filepath, mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            #print(', '.join(row))
            print(row)

def main():
    filepath = input('Please enter the file path:')
    filename, file_ext = os.path.splitext(filepath)

    if file_ext == '.json':
        # json文件
        process_json_file(filepath)
    elif file_ext == '.csv':
        # csv文件
        process_csv_file(filepath)
    else:
        print('Unsupported file format！')

if __name__ == '__main__':
    main()
