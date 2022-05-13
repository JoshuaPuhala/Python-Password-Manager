#PW Generator for PWManager V1
from random import randint, choice
import string
from passwordmeter import test
import pyperclip
import InputValidation as iv

#Allowed special chars for password creation
special_chars = ['!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
                '<', '>', ',', '.', '/', ':', ';', "'", '"', '-', '_', '+', '=']


def create_pw(pw_length): #the password generator
    pass_str = ''
    alpha = list(string.ascii_lowercase) #store the alphabet
    symbols = special_chars
    accepted = False

    while not accepted:
        pass_str = ''
        for i in range(pw_length):
            up_low = randint(0,16)
            if up_low in range(0,4):
                pass_str += choice(alpha).upper()
                i += 1
            elif up_low in range(4,9):
                pass_str += choice(alpha).lower()
                i += 1
            elif up_low in range(9,14):
                pass_str += str(randint(0,9))
                i += 1
            else:
                pass_str += choice(symbols)
                i += 1

        strength,_ = test(pass_str)
        print('\nPassword: %s'%pass_str)
        print('Strength Rating(1.0 is a "perfect" password): %0.5f'%strength)
        if strength < 0.8:
            print('*Passwords with a strength rating below 0.8 are not recommended for use. \n')
        accepted = iv.get_yes_or_no('Accept generated password(if no, a new password will be generated)? \n')
    if accepted:
        pyperclip.copy(pass_str) #copy password to clipboard
        print('-'*40)
        print('Your password has been created and copied to the clipboard!')
        print('-' *40)
        return pass_str