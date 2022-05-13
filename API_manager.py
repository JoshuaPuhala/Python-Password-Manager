#API Manager for PWManager V1
import requests
from hashlib import sha1

### Scanner can be used by itself by uncommenting the following code.
### API key included for later features
#import InputValidation as iv
#password = iv.get_string("Enter the password to be checked: \n")
#API_key = '5d2c2d10fb0440a0afc576e3c544f186'

def convert_pass(password): #encodes the password into utf-8, turns it into sha1 hash
    password = sha1(password.encode('utf8'))
    pass_str = password.hexdigest()
    return pass_str



def scanAPI(passw): #make API call using requests
    """HIBP API call function."""
    pass_str = convert_pass(passw)
    pass_prefix = pass_str[0:5]
    pass_suffix = pass_str[5:].upper()
    hash_dict = {}
    #HIBP asks that we use the range search for improved performance
    response = requests.get(f'https://api.pwnedpasswords.com/range/{pass_prefix}')
    hash_list = response.text.split('\r\n') #split up response by newlines
    for passw in hash_list:
        hash = passw.split(":")
        hash_dict[hash[0]] = hash[1] #turn split up response into a dictionary
    if pass_suffix in hash_dict.keys(): #check keys(the hashes) for matches to our suffix
        print(
            'Password has been found in at least {0} data breaches!'.format(hash_dict[pass_suffix]))
        print('It is recommended that you stop using this password immediately.\n')
    else:
        print(
            'Password not found! Safe to use! \n')
        