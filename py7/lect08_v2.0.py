"""
    Author:Arvin Shaffer
    Function:Simulate throwing a dice and outputting the result
    Version:2.0
    Date:02/27/2018
    2.0 New Function:Simulate two dice
"""
import random

def roll_dice():
    """
    Simulate throwing a dice and outputting the result
    :return:
    """
    roll = random.randint(1, 6)
    return roll

def main():
    total_times = 10000
    result_list = [0] * 11
    roll_list = list(range(2, 13))
    print(roll_list)
    roll_dict = dict(zip(roll_list, result_list))
    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll_dict[roll1 + roll2] += 1
    for i,res in roll_dict.items():
        print("Number of points {}:{},frequency:{}".format(i, res, res/total_times))
    print(roll_dict)


if __name__ == '__main__':
    main()