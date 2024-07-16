from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import BackEnd
#import index
# center the main window according to screen
def centerWindow(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    x = int((screenwidth - width)/2)
    y = int((screenheight - height)/2)
    root.geometry(f"{width}x{height}+{x}+{y}")
#***************  create mainform called root  with no resizable ,centered window *******
root=Tk()
root_width=1300
root_height=600
blankspace=' '
root.title(180*blankspace +'SuperMarket Management System')
centerWindow(root,root_width,root_height)
root.resizable(False,False)
"""def back_():
    # root.destroy()
     import login 
"""
#****************  create main frames **********************************
mainframe=Frame(root,width=root_width,height=root_height,bg='#3e2b3f')
mainframe.grid()

#top frame for title
#titleFrame=Frame(mainframe,bd=7,width=1300,height=80,relief=RIDGE)
#titleFrame.grid(row=0,column=0)

#middle frame for entries and treeview
#topframe3
middleFrame=Frame(mainframe,bd=7,width=1300,height=500,relief=RIDGE,bg='#3e2b3f')
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
bottomFrame=Frame(mainframe,bd=7,width=1300,height=40,relief=RIDGE)
bottomFrame.grid(row=2,column=0,pady=8)

#**************** make title **********************************
#titleLabel=Label(titleFrame,font=('arial',45),text='SuperMarket Management system')
#titleLabel.grid(row=0,column=0,padx=185)



#**************** make TreeView to display data **********************************

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


#****************   add labels ****************************************************
bill_lbl=Label(leftMiddleFrame,font=('arial',11,'bold'),text='Bill No.')
bill_lbl.grid(row=0,column=0,padx=10,pady=10)
bill_en=Entry(leftMiddleFrame,bd=5,font=('arial',11,'bold'),width=25)
bill_en.grid(row=0,column=1,padx=10,pady=10)

name_lbl=Label(leftMiddleFrame,font=('arial',11,'bold'),text='Name.')
name_lbl.grid(row=1,column=0,padx=10,pady=10)
name_en=Entry(leftMiddleFrame,bd=5,font=('arial',11,'bold'),width=25)
name_en.grid(row=1,column=1,padx=10,pady=10)

mobile_lbl=Label(leftMiddleFrame,font=('arial',11,'bold'),text='Mobile.')
mobile_lbl.grid(row=2,column=0,padx=10,pady=10)
mobile_en=Entry(leftMiddleFrame,bd=5,font=('arial',11,'bold'),width=25)
mobile_en.grid(row=2,column=1,padx=10,pady=10)

total_lbl=Label(leftMiddleFrame,font=('arial',11,'bold'),text='Total.')
total_lbl.grid(row=3,column=0,padx=10,pady=10)
total_en=Entry(leftMiddleFrame,bd=5,font=('arial',11,'bold'),width=25)
total_en.grid(row=3,column=1,padx=10,pady=10)

totalfood_lbl=Label(leftMiddleFrame,font=('arial',11,'bold'),text='Total food.')
totalfood_lbl.grid(row=4,column=0,padx=10,pady=10)
totalfood_en=Entry(leftMiddleFrame,bd=5,font=('arial',11,'bold'),width=25)
totalfood_en.grid(row=4,column=1,padx=10,pady=10)

totalgroc_lbl=Label(leftMiddleFrame,font=('arial',11,'bold'),text='Total groc.')
totalgroc_lbl.grid(row=5,column=0,padx=10,pady=10)
totalgroc_en=Entry(leftMiddleFrame,bd=5,font=('arial',11,'bold'),width=25)
totalgroc_en.grid(row=5,column=1,padx=10,pady=10)

totalothers_lbl=Label(leftMiddleFrame,font=('arial',11,'bold'),text='Other Total.')
totalothers_lbl.grid(row=6,column=0,padx=10,pady=10)
totalothers_en=Entry(leftMiddleFrame,bd=5,font=('arial',11,'bold'),width=25)
totalothers_en.grid(row=6,column=1,padx=10,pady=10)

foodtax_lbl=Label(leftMiddleFrame,font=('arial',11,'bold'),text='Food Tax.')
foodtax_lbl.grid(row=7,column=0,padx=10,pady=10)
foodtax_en=Entry(leftMiddleFrame,bd=5,font=('arial',11,'bold'),width=25)
foodtax_en.grid(row=7,column=1,padx=10,pady=10)

groctax_lbl=Label(leftMiddleFrame,font=('arial',11,'bold'),text='Groc Tax.')
groctax_lbl.grid(row=8,column=0,padx=10,pady=10)
groctax_en=Entry(leftMiddleFrame,bd=5,font=('arial',11,'bold'),width=25)
groctax_en.grid(row=8,column=1,padx=10,pady=10)

otherstax_lbl=Label(leftMiddleFrame,font=('arial',11,'bold'),text='Other Tax.')
otherstax_lbl.grid(row=9,column=0,padx=10,pady=10)
otherstax_en=Entry(leftMiddleFrame,bd=5,font=('arial',11,'bold'),width=25)
otherstax_en.grid(row=9,column=1,padx=10,pady=10)

#*********************Buttons functions **********************#
def displayButton():
    #database()
    result =BackEnd.Display()
    #remove tree view from other display
    Supermarket_SystemList.delete(*Supermarket_SystemList.get_children())
    for row in result:
        Supermarket_SystemList.insert('',END,values=row)

def deleteButton():
    customer_bill_num=bill_en.get()
    if len(customer_bill_num) != 0:
            BackEnd.deletecustomer(customer_bill_num)
            displayButton()
            tkinter.messagebox.showinfo('System','record sucessfully deleted')
    else:
            tkinter.messagebox.showinfo('System','you must enter Bill Number first')
def updateButton():
   if bill_en.get()==''or name_en.get()==''or total_en.get()==''or totalfood_en.get()==''or totalgroc_en.get()==''or totalothers_en.get()==''or foodtax_en.get()==''or groctax_en.get()==''or otherstax_en.get()==''or mobile_en.get()=='':
         tkinter.messagebox.askokcancel('System','please fill all data required')
   else:
       BackEnd.updateSupermarket(
            bill_en.get(),
            name_en.get(),
            total_en.get(),
            totalfood_en.get(),
            totalgroc_en.get(),
            totalothers_en.get(),
            foodtax_en.get(),
            groctax_en.get(),
            otherstax_en.get(),
            mobile_en.get()
                    )               
       displayButton()            
       tkinter.messagebox.showinfo('System','record sucessfully updated')     

#****************   add Buttons ****************************************************
def exitButton():
    clear=tkinter.messagebox.askyesno('Supermarket Management System','Confirm if you want to Exit')
    if clear>0:
        root.destroy()
        return 
btnfont=('arial',10,'bold')

btnDisplay=Button(bottomFrame,pady=5,bd=4,font=btnfont,text='Display',width=12,command=displayButton)
btnDisplay.grid(row=0,column=1,padx=1)

btnDelete=Button(bottomFrame,pady=5,bd=4,font=btnfont,text='Delete',width=12,command=deleteButton)
btnDelete.grid(row=0,column=2,padx=1)

btnUpdate=Button(bottomFrame,pady=5,bd=4,font=btnfont,text='Update',width=12,command=updateButton)
btnUpdate.grid(row=0,column=3,padx=1)

btnEXit=Button(bottomFrame,pady=5,bd=4,font=btnfont,text='Exit',width=12,command=exitButton)
btnEXit.grid(row=0,column=6,padx=1)

root.mainloop()
