"""
    Author:Arvin Shaffer
    Function:52 Weeks Money Challenge
    Version:1.0
    Date:02/20/2018
"""

def main():
    money_per_week = 10
    i = 1
    increase_money = 10
    total_week = 52
    saving = 0
    while i <= total_week:
        saving += money_per_week
        print('The first {} weeks deposited {} yuan, the cumulative account {} yuan'.format(i, money_per_week, saving))
        money_per_week += increase_money
        i += 1

if __name__ == '__main__':
    main()