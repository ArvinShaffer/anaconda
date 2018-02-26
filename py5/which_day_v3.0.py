"""
    Author:Arvin Shaffer
    Function:Which day? Enter a certain date of a year to determine the day is the first few days of the year
    Version:3.0
    Date:02/26/2018
    2.0 New Function:Replace tuples with lists!
    3.0 New Function:Divide the month into different sets and then operate
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

    _30_days_month_set = {4, 6, 9, 11}
    _31_days_month_set = {1, 3, 5, 7, 8, 10, 12}
    days = day

    for i in range(1, month):
        if i in _30_days_month_set:
            days += 30
        elif i in _31_days_month_set:
            days += 31
        else :
            days += 28
    if is_leap_yea(year) and month > 2:
        days += 1
    print('This is the {} day of {}'.format(days, year))

if __name__ == '__main__':
    main()
