from tkinter import *  
from tkinter import messagebox 
import tkinter.messagebox 
from PIL import ImageTk,Image
wind = Tk()
def centerWindow(wind, width, height):
    screenwidth = wind.winfo_screenwidth()
    screenheight = wind.winfo_screenheight()
    x = int((screenwidth - width)/2)
    y = int((screenheight - height)/2)
    wind.geometry(f"{width}x{height}+{x}+{y}")
bg = Image.open('supermarket.jpg')
bg.thumbnail((1000, 1000))
width, height = bg.size
bg = ImageTk.PhotoImage(bg)
centerWindow(wind,width,height)
blankspace=' '
wind.title(120*blankspace +'SuperMarket Management System')
wind.resizable(False,False)
def exitButton():
    clear=tkinter.messagebox.askyesno('Student Management System','Confirm if you want to Exit')
    if clear>0:
        wind.destroy()
        return
def check():
    if user_entry.get()=="" and password_entry.get()=="":
         messagebox.showinfo("Login System", "Please enter the Username and Password")
    elif user_entry.get()=="":
        messagebox.showinfo("Login System", "Please enter the Username")
    elif password_entry.get()=="":
        messagebox.showinfo("Login System", "Please enter the Password")
    elif user_entry.get()=="admin" and password_entry.get()!="admin123":
        messagebox.showinfo("Login System", "Please enter the correct Password")     
    elif user_entry.get()=="admin" and password_entry.get()=="admin123":
        messagebox.showinfo("Login System", "Login Success")
         
        wind.destroy()
        import login
    elif user_entry.get()=="admin" and password_entry.get()!="admin123":
        messagebox.showinfo("Login System", "Please enter the correct Password") 
    elif user_entry.get()!="admin" and password_entry.get()=="admin123":
        messagebox.showinfo("Login System", "Please enter the correct Username") 
    else:
        messagebox.showinfo("Login System", "Please enter the correct Username and Password")
canvas = Canvas(wind, width=width, height=height, bd=0, highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg, anchor='nw')

user_label=Label(wind,text="Username",background="#a1dbcd",font=("Ariel 18 bold"))
canvas.create_window(280, 130, anchor="nw", window=user_label)
user_entry=Entry(wind,font=("Ariel 18 bold"))
canvas.create_window(450, 130, anchor="nw", window=user_entry)
password_label=Label(wind,text="Password",background="#a1dbcd",font=("Ariel 18 bold"))
password_entry=Entry(wind,font=("Ariel 18 bold"),show="*")
canvas.create_window(280, 210, anchor="nw", window=password_label)
canvas.create_window(450, 210, anchor="nw", window=password_entry)
login=Button(wind,text="Login",width=8,bg='#0B2F3A',fg='#DBA901',font=("Ariel 22 bold"),command=check)
canvas.create_window(410, 320, anchor="nw", window=login)
close=Button(wind,text="close",width=8,bg='#0B2F3A',fg='#DBA901',font=("Ariel 22 bold"),command=exitButton)
canvas.create_window(410, 450, anchor="nw", window=close)
wind.mainloop()
