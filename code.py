import cv2
import os
import string
from stegano import lsb
from stegano.lsb import generators

import customtkinter as cs
import tkinter as tk
import tkinter.messagebox
import tkinterDnD
from tkinter import filedialog as fd

cs.set_ctk_parent_class(tkinterDnD.Tk)
cs.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
cs.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

root=cs.CTk()
root.geometry("1000x500")
root.title("Steganography Software")


def login():
    print("HELLO")

def userInput1():
    userInput1.message = text_2.get(1.0, "end-1c")
def userInput2():
    userInput2.pwd = text_3.get(1.0, "end-1c")

def openFile1():
    f_types1=[('Jpg files','*.jpg'),('PNG files','*.png')]
    openFile1.filepath = fd.askopenfilename(filetypes=f_types1)
    label_1.configure(text=(openFile1.filepath))
def openFile2():
    f_types2=[('Jpg files','*.jpg'),('PNG files','*.png')]
    openFile2.filepath = fd.askopenfilename(filetypes=f_types2)
    label_3.configure(text=(openFile2.filepath))

def steganography_encryption():
    secret_img = lsb.hide(openFile1.filepath, userInput1.message,generators.eratosthenes())
    secret_img.save("Encryptedmsg2.png")
    img_key = cv2.imread("Encryptedmsg2.png")
    print(str(img_key[0,0,0])+str(img_key[1,1,1])+str(img_key[2,2,2]))
def steganography_decryption():
    img3=cv2.imread(openFile2.filepath)
    password=str(img3[0,0,0])+str(img3[1,1,1])+str(img3[2,2,2])
    label_6 = cs.CTkLabel(master=tab1,text=password,justify=cs.LEFT)
    label_6.pack(pady=10, padx=10)
    message=lsb.reveal(openFile2.filepath,generators.eratosthenes())
    if password==str(userInput2.pwd):
        print(message)
    else:
        print("Wrong Password")

frame=cs.CTkFrame(master=root)
frame.pack(pady=20,padx=60, fill="both", expand=True)

label = cs.CTkLabel(master=frame, text="Secure your files using Watermark", justify=cs.LEFT)
label.pack(pady=10, padx=10)


tabview_1 = cs.CTkTabview(master=frame, width=400, height=250,)
tabview_1.pack(pady=10, padx=10)

tab1=tabview_1.add("Choose Image")
button1=cs.CTkButton(master=tab1, text="Browse", command=openFile1)
button1.pack(pady=12, padx=10)
label_1 = cs.CTkLabel(master=tab1,text="",justify=cs.LEFT)
label_1.pack(pady=10, padx=10)


tab2=tabview_1.add("Encode")
text_2 = cs.CTkTextbox(master=tab2, width=400, height=70)
text_2.pack(pady=10, padx=10)
text_2.insert("0.0", "Enter your message\n\n\n\n")
button2a=cs.CTkButton(master=tab2, text="DONE", command=userInput1)
button2a.pack(pady=12, padx=10)
button2b=cs.CTkButton(master=tab2, text="Encrypt", command=steganography_encryption)
button2b.pack(pady=12, padx=10)


tab3=tabview_1.add("Decode")
text_3 = cs.CTkTextbox(master=tab3, width=400, height=40)
text_3.pack(pady=10, padx=10)
text_3.insert("0.0", "Enter your Password\n\n\n\n")
label_3 = cs.CTkLabel(master=tab3,text="", justify=cs.LEFT)
label_3.pack(pady=10, padx=10)
button4=cs.CTkButton(master=tab3, text="Browse", command=openFile2)
button4.pack(pady=12, padx=10)
button3a=cs.CTkButton(master=tab3, text="DONE", command=userInput2)
button3a.pack(pady=12, padx=10)
button3b=cs.CTkButton(master=tab3, text="Decrypt", command=steganography_decryption)
button3b.pack(pady=12, padx=10)




root.mainloop()
