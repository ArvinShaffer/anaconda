"""
    Author:Arvin Shaffer
    Function:Which day? Enter a certain date of a year to determine the day is the first few days of the year
    Version:4.0
    Date:02/26/2018
    2.0 New Function:Replace tuples with lists!
    3.0 New Function:Divide the month into different sets and then operate
    4.0 New Function:The month and its corresponding number of days with a dictionary said
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

    month_day_dict = {1:31,2:28,3:31,4:30,
                      5:31,6:30,7:31,8:31,
                      9:30,10:31,11:30,12:31
                      }
    day_month_dict = {30:{4,6,9,11},
                      31:{1,3,5,7,8,10,12}}

    days = day

    for i in range(1, month):
        days += month_day_dict[i]
    if is_leap_yea(year) and month > 2:
        days += 1
    print('This is the {} day of {}'.format(days, year))

if __name__ == '__main__':
    main()
