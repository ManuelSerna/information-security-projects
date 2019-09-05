# Information Security Homework 5
# Manuel Serna-Aguilera
# Password Generator Program
import bcrypt
import hashlib
import pickle

# Generate a 32-bit salt, this method will
def generate_salt():
    salt = bcrypt.gensalt()
    return salt[-4:]

# MAIN

# Take in inputs
user = input("Enter username: ")
password = input("Enter password: ")

# TODO: check if password is at least 2, but no more than 5 char long
if len(password) < 2 and len(password) > 5:
    print("WARNING: PASSWORD TOO SHORT OR TOO LONG.")

# Convert password to bytes and concatenate with salt
byte_pwd = bytes(password, 'utf-8')
salt = generate_salt()
H = hashlib.sha256(byte_pwd+salt)

content = [user, salt, H.hexdigest()]

# Use pickle to place content into file
with open("pwd.txt", "wb+") as file_handle:
    pickle.dump(content, file_handle)
