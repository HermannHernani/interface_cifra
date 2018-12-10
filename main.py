from rsa import *
from des import *

data= "Hello there!"
k= des("SnS!ines", ECB, pad=None, padmode=PAD_PKCS5)

enc_data= k.encrypt(data)
print("texto cifrado: ")
print(enc_data)

dec_data= k.decrypt(enc_data)
key = k.getKey()
print("\n")
print("Texto claro: ")
print(dec_data)

print("\n")
print("Chave usada: ")
print(key)

message = encrypt_message(str(key),14257,11)
decript = decrypt_message(message)

print("\n")
print("Chave cifrada com RSA: ")
print(message)

print("\n")
print("Chave decifrada com RSA: ")
print(decript)

