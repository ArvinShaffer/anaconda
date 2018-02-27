"""
    Author:Arvin Shaffer
    Function:Judge the password strength
    Version:5.0
    Date:02/27/2018
    2.0 New Function:Limit the number of password settings.Cycle terminated
    3.0 New Function:Save the password and strength to the file
    4.0 New Function:Read the saved password
    5.0 New Function:Package related methods as a whole: object-oriented programming,Define a ' password'  tool class!
"""

class PasswordTool:
    """
    Password tools class.
    """
    def __init__(self, password):
        self.password = password
        self.strength_level = 0

    def process_password(self):
        # rule1:Password length requires at least 8 bits!
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('Password length requires at least 8 bits!')
        # rule2:The password requires numbers!
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('The password requires numbers!')
        # rule3:The password requires letters
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('The password requires letters!')

    def check_number_exist(self):
        """
        Determine whether there is a string of numbers
        :return:
        """
        has_number = False
        for x in self.password:
            if x.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_exist(self):
        """
        Determines if the string contains letters
        :return:
        """
        has_letter = False
        for x in self.password:
            if x.isalpha():
                has_letter = True
                break
        return has_letter



def main():
    try_times = 5
    while try_times > 0:
        password = input('Please enter the password:')
        password_tool = PasswordTool(password)
        password_tool.process_password()


        if password_tool.strength_level == 1:
            level = 'weak'
        elif password_tool.strength_level == 2:
            level = 'medium'
        elif password_tool.strength_level == 3:
            level = 'strong'
        f = open('password_3.0.txt', 'a')
        f.write('password:{},level:{}\n'.format(password, level))
        f.close()

        if password_tool.strength_level == 3:
            print('Congratulations! Passcode strength')
            break
        else:
            print('The password strength failed!')
            try_times -= 1
        print()
    if try_times <= 0:
        print('Try too many times, the password setting failed')


if __name__ == '__main__':
    main()

