#PW Manager V1 created by Joshua Puhala
import menu, os
from PWGenerator import create_pw
from Credentials import MasterLogin
from data_manager import find_dicts, storein_accounts
import InputValidation as iv

dir_path = os.path.dirname(os.path.realpath(__file__)) #save current working directory

def main():
    """Main."""
    print('Welcome to the Password Manager V1! \n')
    validated = False
    validated, user = login()
    while user == 'none': #'none' user means login() called signup()
        validated, user = login()
    while not validated: #failed login, retry
        validated, user = login()
    while validated: #successful login
        choice = menu.menu() 
        while choice:
            if choice == '1':
                choice = menu.view_logins(user)
            if choice == '2':
                choice = menu.create(user)
            if choice == '3':
                choice = menu.scan()
            if choice == 'Q':
                print('Thanks for using the Password Manager V1!')
                exit()   


def login():
    """Login or signup for a new account."""
    filename = f'{dir_path}\\users.txt'
    login_attempt = iv.get_string( #login/signup
        'Enter your username to login or Create to make a new account: \n')
    if login_attempt == 'Create': #signup
        signup()
        return False, 'none'
    while login_attempt and login_attempt != 'Create': #login
        account_list = find_dicts(filename, 'rt') #open+read users.txt
        #print(account_list) #uncomment to see passwords at login screen for testing purposes
                            #(in case you dont remember the master password)
        for account in account_list:
            account = dict(account)
            if f'{login_attempt}' in account['username']: #find username              
                    pass_try = iv.get_string('Enter the password for this account: \n')
                    if pass_try == account['password']: #password match check
                        print('Login success!\n')
                        return True, login_attempt
                    else:
                        print('Incorrect password!')
                        return False, login_attempt
        else: #username search failed
            print('Username not found. Feel free to create a new account!')
            return False, login_attempt


def signup():
    """Account creation function."""
    filename = f'{dir_path}\\users.txt'
    account_list = find_dicts(filename, 'rt') #open users.txt for reading
    username = iv.get_string('Please provide a username: ')
    if account_list:
        for account in account_list:
            while username in account["username"]:
                print('Username already in use, try again. \n')
                username = iv.get_string('Please provide a username: ')
    while username == 'Create':
        print('This username is forbidden, try again. \n')
        username = iv.get_string('Please provide a username: ')
    email = iv.get_string('Please provide a user email: ')
    password = iv.get_string(
        'Please provide a password(enter C to create a new password): ')
    if password == 'C':
        pass_len = menu.get_valid_len('Enter password length (8-64): ')
        password = create_pw(pass_len)   
    new_master = MasterLogin(username, email, password) #initialize new MasterLogin object
    storein_accounts(new_master.asdict()) #opens the file and appends the new dictionary
    with open(f'{dir_path}\\{new_master.username}_vault.txt', 'w') as f:
        f.close() #create the users Vault file
    print(
        'Account created! Please login to start filling your vault!')

main()