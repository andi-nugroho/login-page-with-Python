from cProfile import label
from ctypes import sizeof
from email import header
from errno import EDEADLK
import fractions
from tkinter import *
from tkinter import messagebox
import ast
from turtle import textinput
from typing import Sized

window = Tk()
window.title("SigUp")
window.geometry('1050x550+300+200')
window.config(bg='#fff')
window.resizable(False,False)

def signup():
    username = user.get()
    password = code.get()
    conform_password = conform_code.get()

    if password == conform_password:
        try:
            file = open('datasheet.txt', 'r+')
            d = file.read()
            r=ast.literal_eval(d)

            dict2 = {username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open('datasheet.txt', 'w')
            w = file.write(str(r))

            messagebox.showinfo('Signup', 'Successfully Sign Up')
        except:
            file = open('datasheet.txt', 'w')
            pp = str({'Username':'password'}) 
            file.write(pp)
            file.close()

    else:
        messagebox.showerror('Invalid', 'Both Password should match')


def sigin():
    window.destroy()



img = PhotoImage(file='register.png')
Label(window, image=img, border=0, bg='white').place(x=120, y=120)

frame = Frame(window, width=410, height=510, bg='white')
frame.place(x=600,y=5)


heading=Label(frame, text='Sign Up', fg='#242F9B', bg='white', font=('Microsoft Yahei UI Light', 24, 'bold'))
heading.place(x=125, y=15)

##---------------------------------------
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    if user.get() =='':
        user.insert(0, 'Username')

user = Entry(frame, width=30, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 12))
user.place(x=20, y=110)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=348, height=1, bg='black').place(x=17, y=140)

##---------------------------------------
def on_enter(e):
    code.delete(0, 'end')
    

def on_leave(e):
    if code.get() =='':
        code.insert(0, 'Password')


code = Entry(frame, width=30, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 12))
code.place(x=20, y=170)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=348, height=1, bg='black').place(x=17, y=200)

##---------------------------------------
def on_enter(e):
    conform_code.delete(0, 'end')

def on_leave(e):
    if conform_code.get() =='':
        conform_code.insert(0, 'Conform Password')

conform_code = Entry(frame, width=30, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 12))
conform_code.place(x=20, y=230)
conform_code.insert(0, 'Conform Password')
conform_code.bind('<FocusIn>', on_enter)
conform_code.bind('<FocusOut>', on_leave)

Frame(frame, width=348, height=1, bg='black').place(x=17, y=260)


##-------------------------------------------


Button(frame, width=25, pady=7, text='Sign Up', font=11, bg='#57a1f8', fg='white', border=0, command=signup).place(x=80, y=330)
label = Label(frame, text='I have an account!', fg='black', bg='white', font=('Microsoft Yahei UI Light', 12))
label.place(x=90, y=380)

sigin = Button(frame, width=6, text='Sign In',font=11, border=0, bg='white', cursor='hand2', fg='#57a1f8')
sigin.place(x=240, y=380)




window.mainloop()