'''
Information Security Homework 3 Part 6
Author: Manuel Serna-Aguilera

    - Verify RSA signature generation
'''
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA 
import time

# Extract private key to sign
f = open('private_key.pem', 'rb')
private_key = RSA.importKey(f.read())
f.close()


# Data to encode -- input from the user
m = input("Write a 7-byte message:\n")

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

# Use private key to get the signature 100 times
sum_time = 0

h = SHA.new(data)
signer = PKCS1_v1_5.new(private_key)

#-----------------------------------------------------
# Measure average time needed for signature generation
#-----------------------------------------------------
for i in range(100):
    initial = time.time()    
    signature = signer.sign(h)
    final = time.time()
    sum_time += (final - initial)

avg_sum = sum_time/100
print("Average time for RSA digital signature generation: ", avg_sum)

# Get public key from a file
f = open('public_key.pem', 'rb')
importedPublicKey = f.read()
f.close()
public_key = RSA.importKey(importedPublicKey)

# Already have data, create verifier object
verifier = PKCS1_v1_5.new(public_key)

#-----------------------------------------------------
# Measure average time needed for signature verification
#-----------------------------------------------------
sum_time = 0
for i in range(100):
    initial = time.time()
    verifier.verify(h, signature)
    final = time.time()
    sum_time += (final - initial)

avg_time = sum_time/100
print("Average time for verification: ", avg_time)
