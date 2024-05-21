from tkinter import *
import random
import string

def get_pass():
    pass1 = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(pass1) for _ in range(pwd_len.get()))
    passstr.set(password)

root = Tk()
root.geometry("400x200")
root.title("Random Password Generator")

passstr = StringVar()
pwd_len = IntVar()

Label(root, text="Password Generator", font="calibri 18 bold").pack(pady=10)
Label(root, text="Enter length of Password").pack(pady=5)
Entry(root, textvariable=pwd_len).pack(pady=5)
Button(root, text="Generate Password", command=get_pass).pack(pady=15)
Entry(root, textvariable=passstr).pack(pady=5)

root.mainloop()
