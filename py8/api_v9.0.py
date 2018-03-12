"""
    Author:Arvin Shaffer
    Function:Air Quality Index Calculation
    Version:9.0
    Date:03/12/2018
    2.0 New Function:use json
    3.0 New Function:read json file and write to csv file
    4.0 New Function:According to the input file to determine whether json or csv, and the corresponding operation
    5.0 New Function:Crawl the web
    6.0 New Function:Use Beautifulsoup4 for data cleaning
    7.0 New Function:Get All Cities AQI
    8.0 New Function:Get All Cities AQI and write to files
    9.0 New Function:use pandas to analysis data
"""
import pandas as pd

def main():
    aqi_data = pd.read_csv('china_city_aqi.csv')
    #print(aqi_data.head(5))
    #print(aqi_data['AQI'])
    #print(aqi_data[['City','AQI']])
    #print('Basic Information：')
    #print(aqi_data.info())

    print('Data preview：')
    print(aqi_data.head())

    # Basic Statistics
    print('AQI Maximum:', aqi_data['AQI'].max())
    print('AQI Min：', aqi_data['AQI'].min())
    print('AQI Average Value：', aqi_data['AQI'].mean())

    # top10
    top10_cities = aqi_data.sort_values(by=['AQI']).head(10)
    print('10 cities with the best air quality：')
    print(top10_cities)

    # bottom10
    # bottom10_cities = aqi_data.sort_values(by=['AQI']).tail(10)
    bottom10_cities = aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print('10 cities with the worst air quality：')
    print(bottom10_cities)

    # Save csv file
    top10_cities.to_csv('top10_aqi.csv', index=False)
    bottom10_cities.to_csv('bottom10_aqi.csv', index=False)

if __name__ == '__main__':
    main()
