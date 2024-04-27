from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb  # pip install stegano

root = Tk()
root.title("Steganography - Hide a secret text message in an image")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg="#2f4155")

def showimage():
    global img
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file",
                                          filetypes=(("PNG file", "*.png"), ("JPG file", "*.jpg"), ("All files", "*.*")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img

def Hide():
    global secret
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file",
                                          filetypes=(("PNG file", "*.png"), ("JPG file", "*.jpg"), ("All files", "*.*")))
    message = text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)
    secret.save("hidden.png")

def show():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file",
                                          filetypes=(("PNG file", "*.png"), ("JPG file", "*.jpg"), ("All files", "*.*")))
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)

def save():
    secret.save("hidden.png")

# icon
image_icon = PhotoImage(file="")

# logo
logo = PhotoImage(file="")
Label(root, image=logo, bg="#2f4155").place(x=10, y=0)

Label(root, text="CYBER SCIENCE", bg="#2f4155", fg="white", font="arial 25 bold").place(x=100, y=20)

# first frame
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)

lbl = Label(f, bg="black")
lbl.place(x=40, y=10)

# second frame
frame2 = Frame(root, bd=3, bg="white", width=340, height=280, relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Roboto 20", bg="white", fg="black", relief=GROOVE)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# third frame
frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=20, y=30 `command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save).place(x=180, y=30)
Label(frame3, text="Picture, Image, Photo file", bg="#2f4155", fg="yellow").place(x=20, y=5)

# fourth frame
frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide data", width=10, height=2, font="arial 14 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Show data", width=10, height=2, font="arial 14 bold", command=show).place(x=180, y=30)
Label(frame4, text="Picture, Image, Photo file", bg="#2f4155", fg="yellow").place(x=20, y=5)

root.mainloop()