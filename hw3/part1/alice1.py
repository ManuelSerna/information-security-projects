'''
Information Security Homework 3 Part 1
Author: Manuel Serna-Aguilera

Alice:
    - encrypt (using CBC mode) 18-byte message m using AES
    - write ciphertext into a file called ctext
'''
from Crypto.Cipher import AES
from Crypto import Random

print("Alice encrypts a message.")

# Read 128 bit key that Alice and Bob share
key = b'sixteen byte key'

# Create initialization vector since we are using CBC mode encryption
# Then make it of AES block size (128-bit)
iv = b'0000111100001111'

# Create cipher using CBC mode, shared secret key, and with an iv
aes = AES.new(key, AES.MODE_CBC, iv)

# Data to encode -- input from the user
# example: "attack business!!!"
m = input("Write an 18-byte message: ")

# Pad the message
if (len(m) <= 18):
    for i in range(len(m), 32):
        m += " "
elif (len(m) > 18):
    m = m[:18]
    for i in range(len(m), 32):
        m += " "
    
#print(len(m)) # length of message (padded = 32 bytes)

# Convert from string to bytes
data = bytes(m, 'utf-8')

# Encrypt message
cipher = aes.encrypt(data)

# Print derived ciphertext
print("Encrypted message: ", cipher)

# Write message m to a file ctext.txt
# second arg: permission, w means write, + means create file if not present
f = open("ctext", "wb+")

f.write(cipher)
# Note: can include iv not encrypted in the file so Bob can get it
f.close()
print("Alice is done.")
