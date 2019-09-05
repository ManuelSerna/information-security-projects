'''
Information Security Homework 3 Part 3
Author: Manuel Serna-Aguilera

- Testing RSA encryption and decryption time
'''
import time 
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

print("\nRSA testing.")

# Generate key
key = RSA.generate(2048)    
public_key = key.publickey()

# Get user input
m = input("Write a 7-byte message: ")

# Pad the message
if (len(m) <= 7):
    for i in range(len(m), 16):
        m += " "
elif (len(m) > 7):
    m = m[:7]
    for i in range(len(m), 16):
        m += " "

# Convert input to byte data type
data = bytes(m, 'utf-8')

e_time = []
d_time = []

for i in range(1, 100):
    # Encrypt message
    e_initial = time.time() # start time of encryption
    cipher = public_key.encrypt(data, 32)
    e_final = time.time() # end encrypting
    e_time.append(e_final - e_initial)

    # Decrypt
    d_initial = time.time()
    decrypted = key.decrypt(cipher)
    d_final = time.time()
    d_time.append(d_final - d_initial)

# Measure average time needed for one encryption
e_sum = 0
for i in e_time:
    e_sum += i

# Measure everage time needed for one decryption
d_sum = 0
for i in d_time:
    d_sum += i

print('Average time for encrypting: ', e_sum/len(e_time))
print('Average time for decrypting: ', d_sum/len(d_time))
print("----------------------------------------------\n")
