"""
A password generator made in Python that generates
a password of length 6-20 characters (inclusive).
"""

from random import randrange

url = 'https://github.com/wickkan'  # GitHub Link
pass_lst = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~`! @#$%^&*()_-+={[}]|\:;"<,>.?/'''  # list that stores all of the possible characters in a password


def ui():
    """
    The user interface
    """
    print('------------------' + '\033[1m' + '\033[92m' + ' PASSWORD GENERATOR ' + '\033[0m' + '------------------')
    print('\033[1m' + 'Choose a password of length 6-20 characters.' + '\033[0m')
    x = None
    while x is None:
        try:
            x = int(input("Enter the length of your desired password: "))
            if 6 > x or x > 20:
                print('\033[1m' + "You must choose a length that is between 6-20 characters (inclusive)." + '\033[0m')
                x = None
        except ValueError:
            print('\033[1m' + "No non-integers or whitespace permitted!" + '\033[0m')
    pass_gen(x)
    print(
        '*****----------------------------------------------*****\n''Thanks for trying: Password Generator\n''Click the link to check out more of my projects:\n',
        url)
    print('*****----------------------------------------------*****')


def pass_gen(length):
    """
    Where the password will be generated
    """
    assert 6 <= length <= 20, "Password length must be between 6-20 characters!"
    assert type(length) == int, "'length' argument must be an integer!"
    # write random password generator
    password = ''
    for x in range(length):
        password += pass_lst[randrange(0, 96)]
    return print("Here is your password: " + '\033[91m' + password + '\033[0m')


if __name__ == '__main__':
    ui()
