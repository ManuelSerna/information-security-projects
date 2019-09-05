'''
Information Security Homework 3 Part 4
Author: Manuel Serna-Aguilera

Alice
    - shares 16-byte secret key with Bob
    - generate HMAC of a 18-byte message m using k
    - write the message m as well as the HMAC into a file named mactext
'''
import Crypto
from Crypto.Hash import HMAC
from Crypto.Hash import SHA256

print("\nAlice writes a message and generates HMAC of the message.")

# Get secret key from file
f = open('secret_key.txt', 'r')
secret_key = f.read()
f.close()
secret_key = bytes(secret_key, 'utf-8')

# Data to encode -- input from the user
m = input("Write an 18-byte message: ")

# Pad the message
if (len(m) <= 18):
    for i in range(len(m), 32):
        m += " "
elif (len(m) > 18):
    m = m[:18]
    for i in range(len(m), 32):
        m += " "
        
# Encode message m to byte string from string
data = bytes(m, 'utf-8')
        
h = HMAC.new(secret_key, msg = data, digestmod = Crypto.Hash.SHA256)
hmac = h.digest()
print("Derived HMAC: ", hmac)

# Write message m and HMAC into file mactext
f = open("mactext", "wb+")
f.write(data + hmac)
f.close()

print("Alice is done.\n")
