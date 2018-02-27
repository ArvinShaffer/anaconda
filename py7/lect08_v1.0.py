"""
    Author:Arvin Shaffer
    Function:Simulate throwing a dice and outputting the result
    Version:1.0
    Date:02/27/2018
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
    result_list = [0] * 6

    for i in range(total_times):
        roll = roll_dice()
        result_list[roll-1] += 1
    for i,res in enumerate(result_list):
        print("Number of points {}:{},frequency:{}".format(i + 1, res, res/total_times))


if __name__ == '__main__':
    main()