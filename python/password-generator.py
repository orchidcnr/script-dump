import string
import secrets
import pyperclip

# Variables
simple = string.ascii_letters + string.digits
complex = simple + string.punctuation

# Questions
try:
    size = int(input("How many characters would you like your password to be? "))
except ValueError:
    size = input("Please provide an answer in the form of an integer. (¬_¬ ) ")
type = input("Would you like your password to be (s)imple or (c)omplex? ")

# Password generator
while True:
    if type == "s":
        password = ''.join(secrets.choice(simple) for i in range (int(size)))
        print(password)
        pyperclip.copy(password)
    elif type == "c":
        password = ''.join(secrets.choice(complex) for i in range (int(size)))
        print(password)
        pyperclip.copy(password)
    else:
        type = input('The answer you provided means nothing to my python script headass. Please provide an answer containing either "s" or "c". Also, you look great today! (≧◡≦)♡ ')
        continue
    # Regenerate password
    again = input("Generate again? (y/n) ")
    if again == "y":
        True
    else:
        break
