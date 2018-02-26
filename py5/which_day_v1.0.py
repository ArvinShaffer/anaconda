"""
    Author:Arvin Shaffer
    Function:Which day? Enter a certain date of a year to determine the day is the first few days of the year
    Version:1.0
    Date:02/26/2018
"""
from datetime import datetime

def main():
    input_data_str = input('Please enter the date(yyyy/mm/dd):')
    input_data = datetime.strptime(input_data_str, '%Y/%m/%d')
    #print(input_data)
    year = input_data.year
    month = input_data.month
    day = input_data.day

    #Calculate
    days_in_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = sum(days_in_month_tup[:month-1]) + day

    #To determine whether the leap year
    if (year%400 == 0) or ((year%4==0) and (year%100!=0)):
        if month > 2:
            days += 1
    print('This is the {}th day'.format(days))

if __name__ == '__main__':
    main()
