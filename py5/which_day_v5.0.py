"""
    Author:Arvin Shaffer
    Function:Which day? Enter a certain date of a year to determine the day is the first few days of the year
    Version:5.0
    Date:02/26/2018
    2.0 New Function:Replace tuples with lists!
    3.0 New Function:Divide the month into different sets and then operate
    4.0 New Function:The month and its corresponding number of days with a dictionary said
    5.0 New Function:With a single line of code to achieve functionality
"""
import time

def main():
    days = time.strptime(input('Please enter the date(yyyy/mm/dd):'), '%Y/%m/%d').tm_yday
    print('This is the {} day!'.format(days))

if __name__ == '__main__':
    main()
