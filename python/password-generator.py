import string
import secrets
import pyperclip

# Variables
simple = string.ascii_letters + string.digits
complex = simple + string.punctuation

# Credits and stuff
print("password-generator v1.1.3")

# Questions
while True:
    try:
        size = int(input("How many characters would you like your password to be? "))
    except ValueError:
        print("Please provide an answer in the form of an integer. (¬_¬ ) ")
        continue
    else:
        break
type = input("Would you like your password to be (s)imple or (c)omplex? ")

# Password generator
while True:
    if type == "s":
        password = ''.join(secrets.choice(simple) for i in range(size))
        print(password)
        pyperclip.copy(password)
    elif type == "c":
        password = ''.join(secrets.choice(complex) for i in range(size))
        print(password)
        pyperclip.copy(password)
    else:
        type = input('The answer you provided means nothing to my python script headass. Please provide an answer containing "s" or "c". ')
        continue
    # Regenerate password
    again = input("Copied to clipboard! Generate again? (y/n) ")
    if again == "y":
        True
    else:
        break
