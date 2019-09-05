'''
Information Security Homework 3 Part 5
Author: Manuel Serna-Aguilera

- Bob
    - read sigtext file
    - verifies RSA signature using Alice's public key
'''
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA

print("\nBob will verify the signature.")

# Get Alice's public key from a file
f = open("public_key.pem", "rb")
extracted_key = f.read()
f.close()
alice_public_key = RSA.importKey(extracted_key)

# Read from file, and slice extracted string to get both message (data) and signature
f = open("sigtext", "rb")
incoming = f.read()
f.close()

data = incoming[:32]
signature = incoming[32:]

# Bob uses Alice's public key to generate a signature
h = SHA.new(data)
verifier = PKCS1_v1_5.new(alice_public_key)

# Print whether the verification succeeds
if verifier.verify(h, signature):
    print("The signature is authentic.")
else:
    print("The signature is NOT authentic.")
