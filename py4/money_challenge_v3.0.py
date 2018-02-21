"""
    Author:Arvin Shaffer
    Function:52 Weeks Money Challenge
    Version:3.0
    Date:02/21/2018
    3.0 New Function:use for to record the number of weekly deposits
"""
import math

def main():
    money_per_week = 10
    i = 1
    increase_money = 10
    total_week = 52
    saving = 0

    money_list = []

    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        print('The first {} weeks deposited {} yuan, the cumulative account {} yuan'.format(i + 1, money_per_week, saving))
        money_per_week += increase_money

if __name__ == '__main__':
    main()