from cmath import exp
from tkinter import *
from tkinter import messagebox
import ast

root = Tk()
root.title("SigUp")
root.geometry('1050x550+300+200')
root.config(bg='#fff')
root.resizable(False,False)


img = PhotoImage(file='login.gif')
Label(root, image=img, border=0, bg='white').place(x=-30, y=30)

frame = Frame(root, width=410, height=510, bg='white')
frame.place(x=600,y=5)


heading=Label(frame, text='Sign in', fg='#242F9B', bg='white', font=('Microsoft Yahei UI Light', 24, 'bold'))
heading.place(x=125, y=15)


def signin():
    username = user.get()
    password = code.get()

    if username == 'admin' and password == '123':
        screen = Toplevel(root)
        screen.title('App')
        screen.geometry('1050x550+300+200')
        screen.config(bg='white')

        Label(screen, text='DANCOK', bg='#fff', font=('Microsoft Yahei UI Light', 50, 'bold')).pack(expand=True)

        screen.mainloop()
    
    elif username != 'admin' and password != '123':
        messagebox.showerror('Invalid', 'Invalid username and password')

    elif password != '123':
        messagebox.showerror('Invalid', 'Invalid password')
        
    elif username != 'admin':
        messagebox.showerror('Invalid', 'Invalid username')




##=========================
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    if user.get() =='':
        user.insert(0, 'Username')

user = Entry(frame, width=30, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 12))
user.place(x=20, y=140)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=348, height=1, bg='black').place(x=17, y=170)


##===========================

def on_enter(e):
    code.delete(0, 'end')
    

def on_leave(e):
    if code.get() =='':
        code.insert(0, 'Password')


code = Entry(frame, width=30, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 12))
code.place(x=20, y=200)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=348, height=1, bg='black').place(x=17, y=230)


##==============

Button(frame, width=29, pady=7, text='Sign In', font=11, bg='#57a1f8', fg='white', border=0, command=signin).place(x=17, y=280)
label = Label(frame, text='I have an account!', fg='black', bg='white', font=('Microsoft Yahei UI Light', 12))
label.place(x=90, y=330)

signup = Button(frame, width=6, text='Sign Up', font=('Microsoft Yahei UI Light', 11, 'bold'), border=0, bg='white', cursor='hand2', fg='#57a1f8')
signup.place(x=230, y=330)
root.mainloop()
