from rsa import *
import pyDes

data= "Hello there!"
k= pyDes.des("SnS!ines", pyDes.ECB, pad=None, padmode=pyDes.PAD_PKCS5)

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

