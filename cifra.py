import tkinter as tk
from tkinter import messagebox as msg
from tkinter.ttk import Notebook
from rsa import *
from des import *
from md5 import *


class TranslateBook(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Interface da Cifra v1")
        self.geometry("500x300")

        self.notebook = Notebook(self)

        english_tab = tk.Frame(self.notebook)
        italian_tab = tk.Frame(self.notebook)

        self.translate_button = tk.Button(english_tab, text="CIFRAR", command=self.translate)
        self.translate_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.english_entry = tk.Text(english_tab, bg="white", fg="black")
        self.english_entry.pack(side=tk.TOP, expand=1)

        self.italian_copy_button = tk.Button(italian_tab, text="Copiar resultados", command=self.copy_to_clipboard)
        self.italian_copy_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.italian_translation = tk.StringVar(italian_tab)
        self.italian_translation.set("")

        self.italian_label = tk.Label(italian_tab, textvar=self.italian_translation, bg="lightgrey", fg="black")
        self.italian_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.notebook.add(english_tab, text="Texto Claro")
        self.notebook.add(italian_tab, text="Texto Cifrado")

        self.notebook.pack(fill=tk.BOTH, expand=1)

    def translate(self, target_language="it", text=None):
        if not text:
            text = self.english_entry.get(1.0, tk.END)

        url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}".format("en", target_language, text)

        try:
            data= "Hello there!"
            k= des("SnS!ines", ECB, pad=None, padmode=PAD_PKCS5)

            enc_data= k.encrypt(data)
            print("texto cifrado: ")
            print(enc_data)
            print(type(enc_data))

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

            k= des("SnS!ines", ECB, pad=None, padmode=PAD_PKCS5)
            enc_data= k.encrypt(text)
            dec_data= k.decrypt(enc_data)
            hashe = md5(text)
            key = k.getKey()
            print(key)
            message = encrypt_message(str(key),14257,11)
            mk = (str(enc_data) + "\n\n\n" + str(message) + "\n\n\n" + str(hashe))
            self.italian_translation.set(mk)
            msg.showinfo("Cifrado", "Texto cifrado com sucesso")
        except Exception as e:
            msg.showerror("A cifra falhou", str(e))

    def copy_to_clipboard(self, text=None):
        if not text:
            text = self.italian_translation.get()

        self.clipboard_clear()
        self.clipboard_append(text)
        msg.showinfo("Copied Successfully", "Text copied to clipboard")


if __name__ == "__main__":
    translatebook = TranslateBook()
    translatebook.mainloop()
