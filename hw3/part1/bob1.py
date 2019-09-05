'''
Information Security Homework 3 Part 1
Author: Manuel Serna-Aguilera

Bob:
    - read ctext file
    - decrypt ciphertext within file
    - output message on the console
'''
from Crypto.Cipher import AES
from Crypto import Random

print("\nBob decrypts a message.")

key = b'sixteen byte key' # shared secret key
iv = b'0000111100001111' # shared iv

# Open and read ctext binary, hence rb
f = open('ctext', 'rb')
cipher = f.read()

# Create AESCipher object to decrypt
aes = AES.new(key, AES.MODE_CBC, iv)
decrypted_m = aes.decrypt(cipher)

print("Received ciphertext: ", cipher)
print("Deciphered plaintext: ", decrypted_m)
print("Bob is finished.")
