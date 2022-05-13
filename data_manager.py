#Data Manager for PWManager V1
import os

dir_path = os.path.dirname(os.path.realpath(__file__)) #save current working directory


def storein_vault(master, login):
    """Opens the user's Vault for appending. Adds new login info."""
    login = dict(login)
    with open(f'{dir_path}\{master}_vault.txt', 'a') as f:
        f.write(str(login) + '\n')


def storein_accounts(master):
    """Opens the users.txt file for appending. Adds new master info."""
    with open(f'{dir_path}\\users.txt', 'a') as f:
        f.write(str(master) + '\n')


def find_dicts(filename, openarg='rt'):
    """Opens a file and creates a dictionary for each line. 
        Returns all dictionaries in a list."""
    account_list = []
    with open(filename, openarg) as users:
        lines = users.read().split('\n')
        for line in lines:
            if line:
                account = create_dict(line)
                account_list.append(account)
    return account_list


def create_dict(d):
    """Receives a dictionary as a string and strips it of all unnecessary 
        punctuation to be returned as a clean dictionary."""
    account = dict()
    pairs = d.strip('{}').split(', ')
    for i in pairs:
        pair = i.split(': ')
        account[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
    return account