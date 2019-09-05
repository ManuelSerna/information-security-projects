'''
Information Security Homework 3 Part 2
Author: Manuel Serna-Aguilera

Alice (encryption):
    - already has Bob's public key
        - 2048-bit = 617 characters long
        (take log base 10 of 2^2048)
    - encrypt message m using Bob's public key
    - write ciphertext to a file named "ctext"
'''
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

print("Alice will encrypt a message using RSA.\nWith Bob's public key.")

# Data to encode -- input from the user
m = input("Write a 18-byte message:\n")

# Pad the message
if (len(m) <= 18):
    for i in range(len(m), 32):
        m += " "
elif (len(m) > 18):
    m = m[:18]
    for i in range(len(m), 32):
        m += " "

# Convert input to byte data type
data = bytes(m, 'utf-8')

# Get Bob's public key from a file
f = open("bob_public_key.pem", "rb")
extracted_key = f.read()
bob_public_key = RSA.importKey(extracted_key)

# Use Bob's public key for Alice to encrypt her message
cipher = bob_public_key.encrypt(data, 32)

f = open('ctext', 'wb+')
f.write(cipher[0]) # write ciphertext to file
f.close()

print("Derived ciphertext: ", cipher)
print("Alice is done.")
