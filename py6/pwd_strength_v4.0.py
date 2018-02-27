"""
    Author:Arvin Shaffer
    Function:Judge the password strength
    Version:4.0
    Date:02/27/2018
    2.0 New Function:Limit the number of password settings.Cycle terminated
    3.0 New Function:Save the password and strength to the file
    4.0 New Function:Read the saved password
"""

def check_number_exist(password_str):
    """
    Determine whether there is a string of numbers
    :param password_str:
    :return:
    """
    has_number = False
    for x in password_str:
        if x.isnumeric():
            has_number = True
            break
    return has_number

def check_letter_exist(password_str):
    """
    Determines if the string contains letters
    :param password_str:
    :return:
    """
    has_letter = False
    for x in password_str:
        if x.isalpha():
            has_letter = True
            break
    return has_letter

def main():
    # try_times = 5
    # while try_times > 0:
    #     password = input('Please enter the password:')
    #     strength_level = 0
    #     #rule1:Password length requires at least 8 bits!
    #     if len(password) >= 8:
    #         strength_level += 1
    #     else:
    #         print('Password length requires at least 8 bits!')
    #     #rule2:The password requires numbers!
    #     if check_number_exist(password):
    #         strength_level += 1
    #     else:
    #         print('The password requires numbers!')
    #     #rule3:The password requires letters
    #     if check_letter_exist(password):
    #         strength_level += 1
    #     else:
    #         print('The password requires letters!')
    #
    #     if strength_level == 1:
    #         level = 'weak'
    #     elif strength_level == 2:
    #         level = 'medium'
    #     elif strength_level == 3:
    #         level = 'strong'
    #     f = open('password_3.0.txt', 'a')
    #     f.write('password:{},level:{}\n'.format(password, level))
    #     f.close()
    #
    #     if strength_level == 3:
    #         print('Congratulations! Passcode strength')
    #         break
    #     else:
    #         print('The password strength failed!')
    #         try_times -= 1
    #     print()
    # if try_times <= 0:
    #     print('Try too many times, the password setting failed')

    f = open('password_3.0.txt', 'r')
    #1.read()
    # content = f.read()
    # print(content)
    #2.readline()
    # line = f.readline()
    # print(line)
    #3.readlines()
    i = 1
    # lines = f.readlines()
    # for line in lines:
    #     print('{} read : {}'.format(i, line))
    #     i += 1
    # for line in f.readlines():
    #     print('{} read : {}'.format(i, line))
    #     i += 1
    for line in f:
        print('{} read : {}'.format(i, line))
        i += 1
    f.close()


if __name__ == '__main__':
    main()

