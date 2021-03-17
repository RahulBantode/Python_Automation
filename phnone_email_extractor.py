'''Demonstration of project phone number and email adress extractor
what to do :-
1.  Get the text from clipboard
2.  find the phone number and email address from that text
3.  Copy and paste the all the matched text onto the clipboard

Need :-
    Two module you need in these project
    1.  regex - import re module - for creatation of regular expression
    2.  pyperclip moudle - import pyperclip - for copy and paste the strings.

    1. have to create two regex object one for phone and second for email
    2. then have to match the phone and email format for the clipboard text
    3. and then neatly formated the email and phone string and copy the single string to the clipboard
'''

import pyperclip, re

'''creatation of phone regex'''
phoneRegex = re.compile(r'''(
    (\d{3} | \(\d{3}\))?                # area code
    (\s | - | \.)?                      # seprator
    (\d{3})                             # first three digits after the area code
    (\s | - | \.)?                      # seprator
    (\d{4})                             # last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension question mark preceding grp denoted - as optional part
)''', re.VERBOSE)

'''creation of email regex'''
emailRegex = re.compile(r'''(
    [a-zA-Z0-9.%+-]+                    # username
    @                                   # @ special character
    [a-zA-Z0-9.-]+                      # domain name
    (\.[a-zA-Z]{2,4})                   # dot something
)''', re.VERBOSE)


'''pyperclip.paste function will get the text from clipboard and which typed as str and assign to variable
text
'''
text = str(pyperclip.paste())

'''now find the exact matches of text with our regex pattern and display it'''
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] == '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])
    '''groups[0] means whole group of matching'''


'''now you have the list of email and phone in the matches varible list 
u have paste it onto the clipboard and display it
pyperclip.copy() fuction takes only single string as argument not taking the
list of string so here you need to use join method for each matches'''

if len(matches) > 0 :
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard')
    print('\n'.join((matches)))
else:
    print('Not phone number and email address found')





