from Tkinter import *
import tkMessageBox

#n = 14257
#e = 11
#d = 1267
#Tn = 13936

LUT_encryption = dict()
LUT_decryption = dict()

def encrypt_message():
    n = int(entryn.get())
    e = int(entrye.get())
    message = texte.get(1.0, END)
    encrypted_msg = ""
    for i in message:
        if i in LUT_encryption:
            encrypted_msg += LUT_encryption[i]
        else:
            numerize = int(ord(i))
            encrypt = pow(numerize, e, n)
            LUT_encryption[i] = unichr(encrypt)
            encrypted_msg += unichr(encrypt)
    clear_text()
    texte.insert(END, encrypted_msg)
    tkMessageBox.showinfo("Encryption", "Message Encrypted!")
    
def clear_text():
    texte.delete(1.0, END)
    
def clear_text2():
    textd.delete(1.0, END)

    
def decrypt_message():
    d = 1267
    n = 14257
    en_message = textd.get(1.0, END)
    decrypted_msg = ""
    for i in en_message:
        if i in LUT_decryption:
            decrypted_msg += LUT_decryption[i]
        else:
            numerize = ord(i)
            decrypt = pow(numerize, d, n)
            LUT_decryption[i] = unichr(decrypt)
            decrypted_msg += unichr(decrypt)
    clear_text2()
    textd.insert(END, decrypted_msg)
    tkMessageBox.showinfo("Decryption", "Message Decrypted!")
    
def openfileE():
    clear_text()
    f = open("Etext.txt", "r")
    texte.insert (END, f.read())
    f.close()
    
def savefileE():
    f = open('Etext.txt', 'w')
    t = texte.get(1.0, END)
    f.write(t)
    f.close()

def openfileD():
    clear_text2()
    f = open("Dtext.txt", "r")
    textd.insert (END, f.read())
    f.close()
    
def savefileD():  
   f = open('Dtext.txt', 'w')
   t = textd.get(1.0, END)
   f.write(t)
   f.close()
   
    
root = Tk() #gives us a blank canvas object to work with
root.title("RSA")
root.configure(background="light blue")

#EncryptionMenu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfileE)
filemenu.add_separator()
filemenu.add_command(label="Save", command=savefileE)
menubar.add_cascade(label="Encryption", menu=filemenu)

#DecryptionMenu
filemenu2 = Menu(menubar, tearoff=0)
filemenu2.add_command(label="Open", command=openfileD)
filemenu2.add_separator()
filemenu2.add_command(label="Save", command=savefileD)
menubar.add_cascade(label="Decryption", menu=filemenu2)
root.config(menu=menubar)

#Labels
labelEn = Label(root, text="Encryption", bg="light blue")
labelEn.grid(row=0, column=2, sticky=EW)

labelD = Label(root, text="Decryption", bg="light blue")
labelD.grid(row=0, column=8, sticky=EW)

labeln = Label(root, text="n =", bg="light blue")
labeln.grid(row=1, column=0, sticky=EW)

labele = Label(root, text="e =", bg="light blue")
labele.grid(row=1, column=2, sticky=EW)

labelpk = Label(root, text="Public Key: (14257, 11)    ")
labelpk.grid(row=1, column=7, columnspan=2, sticky=EW)

label1 = Label(root, text="         ", bg="light blue")
label1.grid(row=0, column=5)

#Entryboxes
entryn = Entry(root, width=5)
entryn.grid(row=1, column=1)

entrye = Entry(root, width=5)
entrye.grid(row=1, column=3)

#Buttons
buttone = Button(root, text="Encrypt", bg="white", command=encrypt_message)
buttone.grid(row=1, column=4)

buttond = Button(root, text="Decrypt", bg="white", command=decrypt_message)
buttond.grid(row=1, column=10)

#Textboxes
texte = Text(root, height=10, width=3, bg= "light gray")
texte.grid(row=2, column=0, rowspan=5, columnspan=5, sticky=EW)

textd = Text(root, height=10, width=5, bg= "light gray")
textd.grid(row=2, column=6, rowspan=5, columnspan=5, sticky=EW)



mainloop()