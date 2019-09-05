'''
Information Security Homework 3 Part 5
Author: Manuel Serna-Aguilera

- Alice
    - sign 18-byte message
    - ...using private key to get signature s
    - write the message m as well as the signature s into a file named sigtext
'''
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA

print("Alice writes message and signs it.")

# Extract Alice's private key so she can sign
f = open('private_key.pem', 'rb')
private_key = RSA.importKey(f.read())
f.close()

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

# Use private key to get the signature
h = SHA.new(data)
signer = PKCS1_v1_5.new(private_key)
signature = signer.sign(h)

print("RSA signature: ", signature)

# Write message and signature to file
sigtext = data + signature
f = open("sigtext", "wb+")
f.write(sigtext)
f.close()

print("\nAlice is done.")
