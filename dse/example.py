import pyDes

data= "Hello there!"
k= pyDes.des("SnS!ines", pyDes.ECB, pad=None, padmode=pyDes.PAD_PKCS5)

enc_data= k.encrypt(data)
print(enc_data)

dec_data= k.decrypt(enc_data)
print(dec_data)
