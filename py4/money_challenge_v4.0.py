"""
    Author:Arvin Shaffer
    Function:52 Weeks Money Challenge
    Version:4.0
    Date:02/22/2018
    2.0 New Function:Record the number of weekly deposits
    3.0 New Function:use for to record the number of weekly deposits
    4.0 New Function:Flexible set the number of deposits per week, increase the number of deposits and deposit weeks
"""
import math

#saving = 0

def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    #global saving
    saving = 0
    money_list = []
    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        #print('The first {} weeks deposited {} yuan, the cumulative account {} yuan'.format(i + 1, money_per_week, saving))
        money_per_week += increase_money
    #print("save_money_in saving:", saving)
    return saving

def main():
   #global saving
    money_per_week = float(input('Please enter the amount of deposit per week:'))
    increase_money = float(input('Please enter a weekly amount:'))
    total_week = int(input('Please enter the total number of weeks:'))
    #saving = 7
    saving = save_money_in_n_weeks(money_per_week, increase_money, total_week)
    print('main saving:',saving)

if __name__ == '__main__':
    main()