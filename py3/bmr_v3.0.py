"""
    Author:Arvin Shaffer
    Function:BMR Calculator
    Version:3.0
    Date:02/16/2018
    3.0 New Function:Users can enter all the information in a row, with the unit of information output
"""

def main():

    y_or_n = input('Whether to exit the program (y/n)?')
    while y_or_n == 'n':
        #gender、weight(kg)、height(cm)、age
        # gender = input('please enter the gender: ')
        # weight = float(input('please enter the weight(kg): '))
        # height = float(input('please enter the height(cm): '))
        # age = int(input('please enter the age: '))
        print('Please enter the following information,Separate with spaces')
        input_str = input('gender weight(kg) height(cm) age:')
        str_list = input_str.split(' ')
        gender = str_list[0]
        weight = float(str_list[1])
        height = float(str_list[2])
        age = int(str_list[3])
        if gender == 'male':
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == 'female':
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else :
            bmr = -1

        if bmr != -1:
            print('Your gender:{},weight:{}kg,height:{}cm,age:{}'.format(gender,weight,height,age))
            print('Your basal metabolic rate {}(calories)'.format(bmr))
        else :
            print('Temporarily not support this gender')
        print()
        y_or_n = input('Whether to exit the program (y/n)?')

if __name__ == '__main__':
    main()

