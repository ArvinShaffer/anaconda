"""
    Author:Arvin Shaffer
    Function:BMR Calculator
    Version:1.0
    Date:02/16/2018
"""

def main():
    #gender、weight(kg)、height(cm)、age
    gender = 'femfdsle'
    weight = 70
    height = 175
    age = 25

    if gender == 'male':
        bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
    elif gender == 'female':
        bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
    else :
        bmr = -1

    if bmr != -1:
        print('Basal metabolic rate (calories):',bmr)
    else :
        print('Temporarily not support this gender')

if __name__ == '__main__':
    main()

