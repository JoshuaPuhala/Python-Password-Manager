#Menu for PWManager V1
import pyperclip, os
import InputValidation as iv
from data_manager import storein_vault, find_dicts, create_dict
from API_manager import scanAPI
from PWGenerator import create_pw
from Credentials import Login

dir_path = os.path.dirname(os.path.realpath(__file__)) #save current working directory


def menu(): #menu display
    """Menu for PWManager.py"""
    print('-'*40)
    print(('-'*18) + 'Menu'+ ('-' *18))
    print('1. View Vault')
    print('2. Create New Login')
    print('3. Scan Password For Leaks')
    print('Q. Exit')
    print('-'*40)
    return get_valid_menu('Enter Choice: ')


def get_valid_menu(msg):
    """Menu input validation."""
    valid_menu = iv.get_string(msg)

    while is_invalid(valid_menu):
        print('Invalid selection. \n')
        valid_menu = iv.get_string(msg)

    return str(valid_menu)


def is_invalid(menu_select):
    """Menu input validation."""
    if menu_select in ['1', '2', '3', 'Q']:
        return False
    else:
        return True


def view_logins(username):
    """Displays the user's Vault."""
    filename = f'{dir_path}\{username}_vault.txt'
    logins = find_dicts(filename, 'rt') #opens the vault for reading only
    if logins: #empty check
        print('-'*40)
        print('\nLogins: \n')
        print(
            f'{"APP:":<15}{"USERNAME:":<15}{"EMAIL:":<25}{"PASSWORD:":<15}{"URL:":<25}NOTES:')
        for login in logins:
            login = create_dict(str(login))
            print(f'{login["app"]:<15}{login["username"]:<15}{login["email"]:<25}'
                + f'{login["password"]:<15}{login["url"]:<25}{login["notes"]}')
        copy = iv.get_yes_or_no('Would you like to copy a password to the clipboard? \n')
        if copy:
            copy_pass(logins)
        choice = menu()
        return choice
    else:
        print("No logins stored yet! \n")
        choice = menu()
        return choice
   

def create(user):
    """Add login info to user's Vault."""
    app = iv.get_string(
        'Please provide the name of the site or app you want to create a login for: ')
    username = iv.get_string(
        'Please provide a username for this site/app: ')
    email = iv.get_string(
        'Please provide a user email for this site/app: ')
    password = iv.get_string(
        'Please provide a password for this site/app(enter C to create new password): ')
    if password == 'C': #password creation check
        pass_len = get_valid_len('Enter password length (8-24): ')
        password = create_pw(pass_len)
    url = iv.get_string(
        'Please paste the url to the site that you are creating this login for: ')
    notes = iv.get_string(
        'Please enter any relevant notes regarding this account(type "none" or "NA" if no note): ')
    while notes in [app, username, email, password, url]:
        print('Notes may not contain duplicate user info!')
        notes = iv.get_string(
        'Please enter any relevant notes regarding this account(type "none" or "NA" if no note): ')
    new_login = Login(app, username, email, password, url, notes) #initialize new login object
    storein_vault(user, new_login.asdict()) #write new data to user's vault
    print('Login created!')
    choice = menu()
    return choice


def get_valid_len(msg):
    """Length input validation."""
    valid_len = iv.get_integer(msg)

    while is_invalid_len(valid_len):
        print('Invalid value. ')
        valid_len = iv.get_integer(msg)
    return valid_len


def is_invalid_len(len):
    """Length input validation."""
    if len > 24:
        print('Enter a length between 8-24: ')
        return True
    if len < 8:
        print('Enter a length between 8-24: ')
        return True
    return False


def scan():
    """Call the API manager, passing the user's input as search parameter."""
    password = iv.get_string('Enter password to be checked: \n')
    scanAPI(password) #pass input to API search
    choice = menu()
    return choice


def copy_pass(dict_list):
    """Copy a password to the clipboard. """
    selection = iv.get_string( #copy password for an account
            'Enter an app, username, email or URL to copy the password for that login to the clipboard. \n' +
            'Enter "back" to return to the menu. \n')
    while selection.lower() != 'back':    
        for login in dict_list:
            if selection in login.values():
                if selection != login['notes']:
                    print(login["password"])
                    pyperclip.copy(login["password"]) #password copied    
                    print('Copied!')
                    return
                else:
                    continue
        else:
            print('Invalid selection! \n')
            selection = iv.get_string( #copy password for an account
                    'Enter an app, username, email or URL to copy the password for that login to the clipboard. \n' +
                    'Enter "back" to return to the menu. \n')
    if selection.lower() == 'back':
        return