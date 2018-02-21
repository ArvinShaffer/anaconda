"""
    Author:Arvin Shaffer
    Function:52 Weeks Money Challenge
    Version:5.0
    Date:02/22/2018
    2.0 New Function:Record the number of weekly deposits
    3.0 New Function:use for to record the number of weekly deposits
    4.0 New Function:Flexible set the number of deposits per week, increase the number of deposits and deposit weeks
    5.0 New Function:According to the date entered by the user to determine the first few weeks of the year, and then output the corresponding deposit amount
"""
import math
import datetime

#saving = 0

def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    #global saving
    saving = 0
    money_list = []
    saved_money_list = []
    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        saved_money_list.append(saving)
        #print('The first {} weeks deposited {} yuan, the cumulative account {} yuan'.format(i + 1, money_per_week, saving))
        money_per_week += increase_money
    #print("save_money_in saving:", saving)
    return saved_money_list

def main():
   #global saving
    money_per_week = float(input('Please enter the amount of deposit per week:'))
    increase_money = float(input('Please enter a weekly amount:'))
    total_week = int(input('Please enter the total number of weeks:'))
    #saving = 7
    saved_money_list = save_money_in_n_weeks(money_per_week, increase_money, total_week)
    input_date_str = input('Please enter the date(yyyy/mm/dd):')
    input_date = datetime.datetime.strptime(input_date_str, '%Y/%m/%d')
    week_num = input_date.isocalendar()[1]
    print('Week {} deposit: {} yuan!'.format(week_num, saved_money_list[week_num - 1]))

if __name__ == '__main__':
    main()