"""
    Author:Arvin Shaffer
    Function:Air Quality Index Calculation
    Version:10.0
    Date:03/12/2018
    2.0 New Function:use json
    3.0 New Function:read json file and write to csv file
    4.0 New Function:According to the input file to determine whether json or csv, and the corresponding operation
    5.0 New Function:Crawl the web
    6.0 New Function:Use Beautifulsoup4 for data cleaning
    7.0 New Function:Get All Cities AQI
    8.0 New Function:Get All Cities AQI and write to files
    9.0 New Function:use pandas to analysis data
    10.0 New Function:use pandas to data cleaning
"""
import pandas as pd
import matplotlib.pyplot as plt
plt.rcdefaults()

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def main():
    aqi_data = pd.read_csv('china_city_aqi.csv')
    print('Basic Information：')
    print(aqi_data.info())

    print('Data preview：')
    print(aqi_data.head())

    # Data
    # Only keep AQI>0 data
    # filter_condition = aqi_data['AQI'] > 0
    # clean_aqi_data = aqi_data[filter_condition]

    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]

    # Basic Statistics
    print('AQI Maximum:', clean_aqi_data['AQI'].max())
    print('AQI Min：', clean_aqi_data['AQI'].min())
    print('AQI Average Value：', clean_aqi_data['AQI'].mean())

    # top50
    top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='bar', x='City', y='AQI', title='50 cities with the best air quality',
                      figsize=(20, 10))
    plt.savefig('top50_aqi_bar.png')
    plt.show()

if __name__ == '__main__':
    main()
