'''
Information Security Homework 3 Part 2
Author: Manuel Serna-Aguilera

Bob (decryption)
    - read from ctext
    - decrypt ciphertext
    - print message
'''
from Crypto.PublicKey import RSA
from Crypto import Random
from pathlib import Path
import ast

print("\nBob will decrypt Alice's message using his private key.")

# Generate public key for Alice to use
my_file = Path("./bob_public_key.pem")

if not(my_file.is_file()):
    key = RSA.generate(2048)
    
    public_key = key.publickey()
    f = open('bob_public_key.pem', 'wb+')
    f.write(public_key.exportKey('PEM'))
    f.close()
    
    f = open('bob_private_key.pem', 'wb+')
    f.write(key.exportKey('PEM'))
    f.close()
    
# Decrypt Alice's message
ctext = Path("./ctext")

if ctext.is_file():
    # Extract encrypted message from ctext
    f = open('ctext', 'rb')
    encrypted_message = f.read()
    f.close()
    
    # Extract private key
    f = open('bob_private_key.pem', 'rb')
    extracted_private_key = f.read()
    f.close()
    
    # Using the extracted private key we got from the file, decrypt Alice's message
    new_private_key = RSA.importKey(extracted_private_key)
    decrypted = new_private_key.decrypt(encrypted_message)
    
    print("Received ciphertext: ", encrypted_message)
    print("Deciphered plaintext: ", decrypted)


print("Bob is done.")
