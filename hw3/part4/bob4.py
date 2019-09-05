'''
Information Security Homework 3 Part 4
Author: Manuel Serna-Aguilera

Bob
    - shares 16-byte secret key with Alice
    - read the message and HMAC from the file
        - verifies the HMAC
        - prints whether the verification succeeds
'''
import Crypto
from Crypto.Hash import HMAC
from Crypto.Hash import SHA256

print("\nBob reads message and verifies HMAC.")

# Get secret key from file
f = open('secret_key.txt', 'r')
secret_key = f.read()
f.close()
secret_key = bytes(secret_key, 'utf-8')

f = open('mactext', 'rb')
incoming = f.read()
f.close()

#print(incoming)
# Message in bytes form
data = incoming[:32]
#print(data)

hmac = incoming[32:]
print("Extracted HMAC: ", hmac)

h = HMAC.new(secret_key, msg = data, digestmod = Crypto.Hash.SHA256)
h = h.digest()

# Check Bob's generated HMAC with HMAC from file to verfiy message integrity
if hmac == h:
    print('HMAC verified.')
else:
    print("Warning: HMAC not verified!")
