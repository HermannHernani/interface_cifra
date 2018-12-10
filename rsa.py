LUT_encryption = dict()
LUT_decryption = dict()

def encrypt_message(message,n,e):
    encrypted_msg = ""
    for i in message:
        if i in LUT_encryption:
            encrypted_msg += LUT_encryption[i]
        else:
            numerize = int(ord(i))
            encrypt = pow(numerize, e, n)
            LUT_encryption[i] = chr(encrypt)
            encrypted_msg += chr(encrypt)
    return encrypted_msg
    
def decrypt_message(en_message):
    d = 1267
    n = 14257
    decrypted_msg = ""
    for i in en_message:
        if i in LUT_decryption:
            decrypted_msg += LUT_decryption[i]
        else:
            numerize = ord(i)
            decrypt = pow(numerize, d, n)
            LUT_decryption[i] = chr(decrypt)
            decrypted_msg += chr(decrypt)
    return decrypted_msg