from tkinter import *
import tkinter.messagebox
class screen2:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1000x700+0+0")
        self.root.maxsize(width = 1000,height = 700)
        self.root.minsize(width = 1000,height = 700)
        blankspace=' '
        self.root.title(150*blankspace +"Supermarket System")
        self.root.resizable(False,False)
        
        ###########################
       
        self.root.configure(bg='#4d004d')
        #========================
        goBill_btn = Button(root,text="Go to bill form",width=20,bg='#6699ff',fg='black',font=("Forte 22 bold"),command=self.goBill)
        goBill_btn.place(relx = 0.5, rely = 0.2, anchor = CENTER)

        #========================
        goUpdate_btn = Button(root,text="Go to updat form",width=20,bg='#6699ff',fg='black',font=("Forte 22 bold"),command=self.goUpate)
        goUpdate_btn.place(relx = 0.5, rely = 0.39, anchor = CENTER)

        #====================
        search_btn = Button(root,text="Search",width=8,bg='#6699ff',fg='black',font=("Forte 22 bold"),command=self.Search)
        search_btn.place(relx = 0.5, rely = 0.58, anchor = CENTER)

        #======================
        def exitButton():
            clear=tkinter.messagebox.askyesno('Student Management System','Confirm if you want to Exit')
            if clear>0:
                root.destroy()
            return
        #===========
        
        exit_btn = Button(root,text="Close",width=8,bg='#6699ff',fg='black',font=("Forte 22 bold"),command=exitButton)
        exit_btn.place(relx = 0.5, rely = 0.77, anchor = CENTER)        
        #########################
        
    def goBill(self):
       self.root.destroy()
       import index
    def goUpate(self):
       self. root.destroy()
       import edit 
    def Search(self):
       self.root.destroy()
       import Search
    ##############################
    

root = Tk()
object = screen2(root)
root.mainloop()