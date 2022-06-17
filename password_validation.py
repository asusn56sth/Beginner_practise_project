# password validation

# password should be between 8 to 20 character long
# password have atleast one number [0-9]
# password must have atleast one uppercase [A-Z]
# password must have atlestt one special character (@,#,$,%,&,*,^)
# password must have atleast one lowercase [a-z]

# ask user for password
password = input("Password :")


def password_validation(password):
    special_character = [
        " ", "@", "#", "$", "%", "!", "~", "^", "&",
        "*", "?", "<", ">", "=", '"', "'", "(", ")",
        "+", ",", "-", ".", "/", ":", ";", "[", "]",
        "\\", "_", "`", "{", "}", "|"
    ]
    # length of password must be 8 to 20character long
    islength_ok = True if len(password) >= 8 and len(password) <= 20 else False
    # returns true if if any one of teh character is digit in the password
    isnumber_present = any(character.isdigit() for character in password)
    # returns true if any of the character is lowercase in the password
    islowercase_present = any(character.islower() for character in password)
    # returns true if any of the character is uppercase in the password
    isuppercase_present = any(character.isupper() for character in password)
    # returns true if any of thecharacter is the special character
    isspecial_present = any(
        character in special_character for character in password)

    # returns true if all the condition are true otherwise false
    # check the validation of the pass word
    isvalid = all([islength_ok, isnumber_present,
                  islowercase_present, isuppercase_present, isspecial_present])

    print("Invalid password" if not isvalid else "Okay")


password_validation(password)
