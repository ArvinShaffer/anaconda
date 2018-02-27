"""
    Author:Arvin Shaffer
    Function:Simulate throwing a dice and outputting the result
    Version:3.0
    Date:02/27/2018
    2.0 New Function:Simulate two dice
    3.0 New Function:Visualization the result of simulate two dice
"""
import random
import matplotlib.pyplot as plt
plt.rcdefaults()

def roll_dice():
    """
    Simulate throwing a dice and outputting the result
    :return:
    """
    roll = random.randint(1, 6)
    return roll

def main():
    total_times = 100
    result_list = [0] * 11
    roll_list = list(range(2, 13))
    roll_dict = dict(zip(roll_list, result_list))
    #record the result of dice
    roll1_list = []
    roll2_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll1_list.append(roll1)
        roll2_list.append(roll2)

        roll_dict[roll1 + roll2] += 1
    for i,res in roll_dict.items():
        print("Number of points {}:{},frequency:{}".format(i, res, res/total_times))

    x = range(1, total_times + 1)
    plt.scatter(x, roll1_list, c='red', alpha=0.5)
    plt.scatter(x, roll2_list, c='green', alpha=0.5)
    plt.show()

if __name__ == '__main__':
    main()
