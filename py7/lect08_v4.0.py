"""
    Author:Arvin Shaffer
    Function:Simulate throwing a dice and outputting the result
    Version:4.0
    Date:02/27/2018
    2.0 New Function:Simulate two dice
    3.0 New Function:Visualization the result of simulate two dice
    4.0 New Function:The results of a simple data statistics and analysis
"""
import random
import matplotlib.pyplot as plt
plt.rcdefaults()

#set Chinese
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def roll_dice():
    """
    Simulate throwing a dice and outputting the result
    :return:
    """
    roll = random.randint(1, 6)
    return roll

def main():
    total_times = 10000
    #record the result of dice
    roll_list = []
    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll_list.append(roll1 + roll2)

    plt.hist(roll_list, bins=range(2, 14), normed=1, edgecolor='black', linewidth=1)
    plt.title('Dice points statistics')
    plt.xlabel('Points')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == '__main__':
    main()
