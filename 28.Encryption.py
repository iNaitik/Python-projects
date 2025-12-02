import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"keys: {key}")

# ENCRYPTION

plain_text = input("Enter your text: ")
encypt = ""

for i in plain_text:
    index = chars.index(i)
    encypt = encypt+key[index]

print(f"Original message: {plain_text}")
print(f"Encrpted message: {encypt}")

#DECRYPTION

encypt = input("Enter your text: ")
plain_text = ""

for i in encypt:
    index = key.index(i)
    plain_text += chars[index]

print(f"Encrpted message: {encypt}")
print(f"Original message: {plain_text}")
