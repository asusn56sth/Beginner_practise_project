# email validation

'''
start with the alphabet must be from [a-z] or numbers [0-9] before @
".", "_" must be used only one time before @
@ must be used only one time
"." must be at 2nd or 3rd from last
for EXAMPLE: abc.company@email.com
'''

import re  # regular expression module

#  ask email id from user
email = input("Enter your email : ")


def email_validation(email):

    # validate the given email id is in particular pattern using regular expression
    email_pattern = "^[a-z]+[\._]?[a-z 0-9]+[@]\D+[.]\w{2,3}$"

    print("Invalid email id" if not re.search(
        email_pattern, email) else "Valid email id")


email_validation(email)
