"""
    Author:Arvin Shaffer
    Function:Simulate throwing a dice and outputting the result
    Version:5.0
    Date:02/27/2018
    2.0 New Function:Simulate two dice
    3.0 New Function:Visualization the result of simulate two dice
    4.0 New Function:The results of a simple data statistics and analysis
    5.0 New Function:Simplify your program with scientific computing libraries to improve your data visualization results
"""
import random
import matplotlib.pyplot as plt
import numpy as np
plt.rcdefaults()

#set Chinese
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def main():
    total_times = 10000
    #record the result of dice
    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    result_arr = roll1_arr + roll2_arr
    hist, bins = np.histogram(result_arr, bins=range(2, 14))
    print(hist)
    print(bins)

    plt.hist(result_arr, bins=range(2, 14), normed=1, edgecolor='black', linewidth=1, rwidth=0.8)
    tick_labels = ['2点', '3点', '4点', '5点',
                   '6点', '7点', '8点', '9点', '10点', '11点', '12点']
    tick_pos = np.arange(2, 13) + 0.5
    plt.xticks(tick_pos, tick_labels)
    plt.title('Dice points statistics')
    plt.xlabel('Points')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == '__main__':
    main()
