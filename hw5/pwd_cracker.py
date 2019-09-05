# Information Security Homework 5
# Manuel Serna-Aguilera
# Password cracker Program

import pickle
import itertools
import string
import hashlib
import time

# Open file with pickle and
with open("pwd.txt", 'rb') as file_handle:
    content = pickle.load(file_handle)

real_user = content[0]
real_salt = content[1]
real_hash = content[2]

# Method to attempt to crack a password given hash stored in database
def guess_password(part):
    # Part 1 domain: lower-case letters only
    domain = string.ascii_lowercase
    if part == '1':
        print("Part 1.")

    # Part 2 domain: add upper-case letters
    elif part == '2':
        domain += string.ascii_uppercase

    # Part 3 domain: add digits
    elif part == '3':
        domain += string.ascii_uppercase + string.digits

    # Part 4 domain: add special
    elif part == '4':
        domain += string.ascii_uppercase + string.digits + '$' + '#' + '%' + '&' + '*' + "(" + ")"

    else:
        return "Error"
    attempts = 0

    # Go through 2 to 5 characters, guessing one correct character at a time
    for password_length in range(2, 6):
        for guess in itertools.product(domain, repeat=password_length):
            attempts += 1
            guess = ''.join(guess) # try out every possible combination from 2...5

            # Hash the guessed password, concatenate with salt from file
            byte_pwd_guess = bytes(guess, 'utf-8')
            guess_H = hashlib.sha256(byte_pwd_guess + real_salt)

            # Compare guess with the read hash (from file)
            if guess_H.hexdigest() == real_hash:
                return 'Password: {}.\nFound in {} guesses.'.format(guess, attempts)
            print(guess, attempts)


# MAIN - guess password
part = input("Enter Homework 5 part (1, 2, 3, or 4): ")

start = time.time()
print(guess_password(part))
finish = time.time() - start
print("Total time (secs): ", finish)