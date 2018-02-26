"""
    Author:Arvin Shaffer
    Function:Which day? Enter a certain date of a year to determine the day is the first few days of the year
    Version:2.0
    Date:02/26/2018
    2.0 New Function:Replace tuples with lists!
"""
from datetime import datetime

def is_leap_yea(year):
    """
    To determine whether a leap year
    Yes, return true
    No, return false
    :param year:
    :return:
    """
    is_leap = False
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True
    return is_leap

def main():
    input_data_str = input('Please enter the date(yyyy/mm/dd):')
    input_data = datetime.strptime(input_data_str, '%Y/%m/%d')
    #print(input_data)
    year = input_data.year
    month = input_data.month
    day = input_data.day

    #Calculate
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_yea(year):
        days_in_month_list[1] = 29
    days = sum(days_in_month_list[:month-1]) + day
    print('This is the {} day of {}'.format(days, year))

if __name__ == '__main__':
    main()
