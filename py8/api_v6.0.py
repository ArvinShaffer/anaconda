"""
    Author:Arvin Shaffer
    Function:Air Quality Index Calculation
    Version:6.0
    Date:03/9/2018
    2.0 New Function:use json
    3.0 New Function:read json file and write to csv file
    4.0 New Function:According to the input file to determine whether json or csv, and the corresponding operation
    5.0 New Function:Crawl the web
    6.0 New Function:Use Beautifulsoup4 for data cleaning
"""
import requests
from bs4 import BeautifulSoup


def get_city_aqi(city_pinyin):
    """
        Get the city's AQI
    """
    url = 'http://pm25.in/' + city_pinyin
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', {'class': 'span1'})

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()

        city_aqi.append((caption, value))
    return city_aqi


def main():
    city_pinyin = input('Please input city Pinyin：')
    city_aqi = get_city_aqi(city_pinyin)
    print(city_aqi)

if __name__ == '__main__':
    main()
