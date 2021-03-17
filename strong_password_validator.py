'''
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase characters,
and has at least one digit. You may need to test the string against multiple
regex patterns to validate its strength.
'''

import re

password = re.compile(r'''(
    ([a-zA-Z0-9@#%&$]{1,8})
    
)''', re.VERBOSE)

input_password = input('Enter the password \t:\t')
verify_password = password.search(input_password)

if verify_password != None:
    if len(verify_password.group()) == 8:
        print('You entered password is strong')
        print('Your password is \t:\t'+ verify_password.group())
    elif len(verify_password.group()) > 8:
        print('You entered password length is bigger than 8')

    else:
        print('You entered password is poor/less strong')
else:
    print('You entered password is poor/less strong')