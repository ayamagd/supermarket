from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3
# center the main window according to screen
def centerWindow(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    x = int((screenwidth - width)/2)
    y = int((screenheight - height)/2)
    root.geometry(f"{width}x{height}+{x}+{y}")
#*****  create mainform called root  with no resizable ,centered window ***
root=Tk()
root_width=1300
root_height=600
blankspace=' '
root.title(180*blankspace +'SuperMarket Management System')
centerWindow(root,root_width,root_height)
root.resizable(False,False)
#******  create main frames ************
mainframe=Frame(root,width=root_width,height=root_height,bg='#3e2b3f')
mainframe.grid()

#top frame for title
titleFrame=Frame(mainframe,bd=7,width=1300,height=100,relief=RIDGE)
titleFrame.grid(row=0,column=0)

#middle frame for entries and treeview
#topframe3
middleFrame=Frame(mainframe,bd=7,width=1300,height=600,relief=RIDGE,bg='#3e2b3f')
middleFrame.grid(row=1,column=0,pady=8)

#this middle separated into two frames
#1-Labels and entries
leftMiddleFrame=Frame(middleFrame,width=100,height=100)
leftMiddleFrame.grid(row=0,column=0,padx=10)
#2-treeView
RightMiddleFrame=Frame(middleFrame,width=1200,height=600)
RightMiddleFrame.grid(row=0,column=1,padx=10)

#bottom frame for buttons
#topframe1
bottomFrame=Frame(mainframe,bd=7,width=1300,height=60,relief=RIDGE)
bottomFrame.grid(row=2,column=0,pady=8)

#****** make title ************
titleLabel=Label(titleFrame,font=('arial',45),text='SuperMarket Management system')
titleLabel.grid(row=0,column=0,padx=185)
#****** make TreeView to display data ************

#help to make capapbility of scrolling data
scroll_x=Scrollbar(RightMiddleFrame,orient=HORIZONTAL)
scroll_y=Scrollbar(RightMiddleFrame,orient=VERTICAL) 

Supermarket_SystemList=ttk.Treeview(RightMiddleFrame,height=18,columns=('BillNo','name','total','TotalFood','TotalGrocery','OthersTotal','FoodTax','GroceryTax','OtherTax','mobile'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.configure(command=Supermarket_SystemList.xview)
scroll_y.configure(command=Supermarket_SystemList.yview)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
Supermarket_SystemList.heading('BillNo',text='Bill Number')
Supermarket_SystemList.heading('name',text=' Name')
Supermarket_SystemList.heading('total',text='total')
Supermarket_SystemList.heading('TotalFood',text='Total Food')
Supermarket_SystemList.heading('TotalGrocery',text='Total Grocery')
Supermarket_SystemList.heading('OthersTotal',text='Others Total')
Supermarket_SystemList.heading('FoodTax',text='Food Tax')
Supermarket_SystemList.heading('GroceryTax',text='Grocery Tax')
Supermarket_SystemList.heading('OtherTax',text='Other Tax')
Supermarket_SystemList.heading('mobile',text='Mobile')

Supermarket_SystemList['show']='headings'


Supermarket_SystemList.column('BillNo',width=80)
Supermarket_SystemList.column('name',width=60)
Supermarket_SystemList.column('total',width=60)
Supermarket_SystemList.column('TotalFood',width=100)
Supermarket_SystemList.column('TotalGrocery',width=100)
Supermarket_SystemList.column('OthersTotal',width=100)
Supermarket_SystemList.column('FoodTax',width=100)
Supermarket_SystemList.column('GroceryTax',width=100)
Supermarket_SystemList.column('OtherTax',width=100)
Supermarket_SystemList.column('mobile',width=80)

Supermarket_SystemList.pack(fill=BOTH,expand=True)

def exitButton():
    clear=tkinter.messagebox.askyesno('Student Management System','Confirm if you want to Exit')
    if clear>0:
        root.destroy()
        return 


def search():
    k=bill_en.get()
    if k!="":
        conn=sqlite3.connect('Supermarket_System.db')
        c=conn.execute("select * from supermarket where BillNo=? ",k)
        a=c.fetchall()
        if len(a)!=0:
           for row in a:
              Supermarket_SystemList.insert("",END,values=row)
           conn.commit()
           conn.close()
        else:
            messagebox.showinfo("Error","Data not found")
    else:
            messagebox.showinfo("Error","Search field cannot be empty.")   
#******   add Buttons ******************

btnfont=('arial',15,'bold')

Search=Button(bottomFrame,pady=5,bd=4,font=btnfont,text='Search',width=12,command=search)
Search.grid(row=0,column=1,padx=1)
# id
bill_lbl=Label(leftMiddleFrame,font=('arial',12,'bold'),text='Bill No.')
bill_lbl.grid(row=0,column=0,padx=10,pady=10)
bill_en=Entry(leftMiddleFrame,bd=5,font=('arial',12,'bold'),width=25)
bill_en.grid(row=0,column=1,padx=10,pady=10)
btnEXit=Button(bottomFrame,pady=5,bd=4,font=btnfont,text='Exit',width=11,command=exitButton)
btnEXit.grid(row=0,column=3,padx=1)
root.mainloop()