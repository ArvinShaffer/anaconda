"""
    Author:Arvin Shaffer
    Function:BMR Calculator
    Version:2.0
    Date:02/16/2018
    2.0 New Function:Calculated based on user input,The program is running continuously
"""

def main():

    y_or_n = input('Whether to exit the program (y/n)?')
    while y_or_n == 'n':
        #gender、weight(kg)、height(cm)、age
        gender = input('please enter the gender: ')
        weight = float(input('please enter the weight(kg): '))
        height = float(input('please enter the height(cm): '))
        age = int(input('please enter the age: '))

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
        print()
        y_or_n = input('Whether to exit the program (y/n)?')

if __name__ == '__main__':
    main()

