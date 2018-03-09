"""
    Author:Arvin Shaffer
    Function:Air Quality Index Calculation
    Version:5.0
    Date:03/9/2018
    2.0 New Function:use json
    3.0 New Function:read json file and write to csv file
    4.0 New Function:According to the input file to determine whether json or csv, and the corresponding operation
    5.0 New Function:Crawl the web
"""
import requests


def get_html_text(url):
    """
        返回url的文本
    """
    r = requests.get(url, timeout=30)
    # print(r.status_code)
    return r.text


def main():
    city_pinyin = input('Please input city Pinyin：')
    url = 'http://pm25.in/' + city_pinyin
    url_text = get_html_text(url)

    # aqi_div = '''<div class="span12 data">'''
    # index = url_text.find(aqi_div)
    # begin_index = index + 96
    # end_index = begin_index + 3
    # # begin_index = index + len(aqi_div)
    # # end_index = begin_index + 2
    # aqi_val = url_text[begin_index: end_index]
    # print('Air quality is：{}'.format(aqi_val))

    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 3
    aqi_val = url_text[begin_index: end_index]
    print('Air quality is：{}'.format(aqi_val))

if __name__ == '__main__':
    main()
