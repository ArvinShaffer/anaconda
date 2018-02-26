"""
    Author:Arvin Shaffer
    Function:Judge the password strength
    Version:1.0
    Date:02/26/2018
"""

def check_number_exist(password_str):
    """
    Determine whether there is a string of numbers
    :param password_str:
    :return:
    """
    for x in password_str:
        if x.isnumeric():
            return True
    return False

def check_letter_exist(password_str):
    """
    Determines if the string contains letters
    :param password_str:
    :return:
    """
    for x in password_str:
        if x.isalpha():
            return True
    return False

def main():
    password = input('Please enter the password:')
    strength_level = 0
    #rule:Password length requires at least 8 bits!
    if len(password) >= 8:
        strength_level += 1
    else:
        print('Password length requires at least 8 bits!')
    #rule2:The password requires numbers!
    if check_number_exist(password):
        strength_level += 1
    else:
        print('The password requires numbers!')
    #rule3:The password requires letters
    if check_letter_exist(password):
        strength_level += 1
    else:
        print('The password requires letters!')

    if strength_level == 3:
        print('Congratulations! Passcode strength')
    else:
        print('The password strength failed!')

if __name__ == '__main__':
    main()

