import string
import secrets

# Question variables
size = input("How many characters would you like your password to be? ")
type = input("Would you like your password to be simple (1) or complex (2)? ")

# Answer variables
simple = string.ascii_letters + string.digits
complex = simple + string.punctuation

# Password generator
while True:
    if type == "1":
        password = ''.join(secrets.choice(simple) for i in range (int(size)))
        print(password)
    if type == "2":
        password = ''.join(secrets.choice(complex) for i in range (int(size)))
        print(password)
    again = input("Generate again? (y/n) ")
    if again != "y":
        break
