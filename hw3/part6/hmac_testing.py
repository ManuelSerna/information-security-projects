'''
Information Security Homework 3 Part 6
Author: Manuel Serna-Aguilera

    - Verify HMAC generation, 
    - signature generation,
    - and signature verification.
'''
import Crypto
from Crypto.Hash import HMAC
from Crypto.Hash import SHA256
import time

print("HMAC testing.")

# Get secret key
secret_key = b'sixteen byte key'

# Data to encode -- input from the user
m = input("Write an 7-byte message: ")

# Pad the message
if (len(m) <= 7):
    for i in range(len(m), 16):
        m += " "
elif (len(m) > 7):
    m = m[:7]
    for i in range(len(m), 16):
        m += " "

# Encode message m to byte string from string
data = bytes(m, 'utf-8')

#-----------------------------------------------------
# Measure average time needed for one HMAC generation
#-----------------------------------------------------
sum_time = 0

for i in range(100):
    initial = time.time()
    h = HMAC.new(secret_key, msg = data, digestmod = Crypto.Hash.SHA256)
    final = time.time()
    sum_time += (final - initial)

avg_time = sum_time/100

print("Average time for HMAC generation: ", avg_time)

#-----------------------------------------------------
# Measure average time needed for one HMAC signature generation
#-----------------------------------------------------
sum_time = 0

for i in range(100):
    initial = time.time()
    hmac = h.hexdigest()
    final = time.time()
    sum_time += (final - initial)
    
avg_time = sum_time/100

print("Average time for HMAC signature generation: ", avg_time)

#-----------------------------------------------------
# Measure average time needed for one HMAC signature verification
#-----------------------------------------------------
sum_time = 0

new_h = HMAC.new(secret_key, msg = data, digestmod = Crypto.Hash.SHA256)
new_hmac = new_h.hexdigest()

for i in range(100):
    initial = time.time()
    if new_hmac == hmac:
        final = time.time()
    sum_time += (final - initial)
    
avg_time = sum_time/100

print("Average time for HMAC signature verification: ", avg_time)
