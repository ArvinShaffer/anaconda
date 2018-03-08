"""
    Author:Arvin Shaffer
    Function:Air Quality Index Calculation
    Version:2.0
    Date:03/8/2018
    2.0 New Function:use json
"""
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
    print(city_list)
    city_list.sort(key=lambda city: city['aqi'])
    print(city_list)
    top5_list = city_list[:5]

    f = open('top5_aqi.json', mode='w', encoding='utf-8')
    json.dump(top5_list, f, ensure_ascii=False)
    f.close()

if __name__ == '__main__':
    main()
