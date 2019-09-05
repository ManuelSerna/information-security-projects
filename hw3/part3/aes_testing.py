'''
Information Security Homework 3 Part 3
Author: Manuel Serna-Aguilera

- Testing AES encryption and decryption time
'''
import time
from Crypto.Cipher import AES
from Crypto import Random

print("\nAES testing.")

# Create 128 bit key that Alice and Bob share
key = b'sixteen byte key'

# Create initialization vector since we are using CBC mode encryption
# Then make it of AES block size (128-bit)
iv = b'0000111100001111'

# Create cipher using CBC mode, shared secret key, and with an iv
aes = AES.new(key, AES.MODE_CBC, iv)

# Data to encode -- input from the user
# example: "attack business!!!"
m = input("Write an 7-byte message: ")

# Pad the message
if (len(m) <= 7):
    for i in range(len(m), 16):
        m += " "
elif (len(m) > 7):
    m = m[:7]
    for i in range(len(m), 16):
        m += " "

# Convert from string to bytes
data = bytes(m, 'utf-8')

# Note: time.time() returns SECONDS
# Keep track of encryption and decryption differences in these arrays
e_time = []
d_time = []

for i in range(1, 100):
    # Encrypt message
    e_initial = time.time() # start time of encryption
    cipher = aes.encrypt(data) # encrypt
    e_final = time.time() # end encrypting
    e_time.append(e_final - e_initial)
    
    # Decrypt message
    d_initial = time.time()
    decrypted_m = aes.decrypt(cipher)
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

print("Average time for encrypting: ", e_sum/len(e_time))
print("Average time for decrypting: ", d_sum/len(d_time))
print("----------------------------------------------\n")
