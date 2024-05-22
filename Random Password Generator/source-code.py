import random
import string
from tkinter import *
from tkinter.font import Font

def generate_password():
    password = []
    for _ in range(2):  # Use `_` since the index `i` is not used
        alpha = random.choice(string.ascii_letters)
        symbol = random.choice(string.punctuation)
        number = random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(number)
    y = "".join(password)
    lbl.config(text=y)

root = Tk()
root.geometry("250x200")
root.title("Password Generator")

btn = Button(root, text="Generate Password", command=generate_password)
btn.place(relx=0.5, rely=0.2, anchor=N)

myFont = Font(family="Times New Roman", size=12)
lbl = Label(root, font=myFont)
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()