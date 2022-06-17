# PASSWORD GENERATOR
# generate a password of specific length which fullfill all the criterias

# generate a random password
import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
special_character = " @#$%!~^&*?<>=\'\"()+,-./:;[]\\_`\{\}|"


uppercase, lowercase, num, specialchar = True, True, True, True

all = ""
# how many letters password do you want.
length = 15

# select true if you want use all teh character otherwise only the ones you want to incorporate in yor password
if uppercase:
    uppercase_letters = ''.join(random.choices(uppercase_letters, k=2))
    all += uppercase_letters
if lowercase:
    lowercase_letters = ''.join(random.choices(lowercase_letters, k=9))
    all += lowercase_letters
if num:
    digits = ''.join(random.choices(digits, k=2))
    all += digits
if specialchar:
    special_character = ''.join(random.choices(special_character, k=2))
    all += special_character


# returns a list of n nos. of character without a repitition and joins them together in a string
password = ''.join(random.sample(all, length))
print(password)
