from tkinter import *
from code import *
from tkinter import ttk
import tkinter.messagebox
import BackEnd
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
root_height=705
blankspace=' '
root.title(180*blankspace +'SuperMarket Management System') 
centerWindow(root,root_width,root_height)
root.resizable(False,False)
cus_name = StringVar()
c_phone = StringVar()     
c_bill_no = StringVar()
bread = IntVar()
candy = IntVar()
hamburger = IntVar()
hotdog = IntVar()
sandwich = IntVar()
rice = IntVar()
salt = IntVar()
food_oil = IntVar()
wheat = IntVar()
sugar = IntVar()
gatorade = IntVar()
coke = IntVar()
juice = IntVar()
waffer = IntVar()
biscuits = IntVar()
total1 = StringVar()
total_food = StringVar()
total_grocery = StringVar()
total_other = StringVar()
tax_cos = StringVar()
tax_groc = StringVar()
tax_other = StringVar()


        #===================================
bg_color = "#3e2b3f"
fg_color = "white"
lbl_color = 'white'
        #Title of App
title = Label(root,text = "Grocery Billing System",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

        #==========Customers Frame==========#
F1 = LabelFrame(text = "Customer Details",font = ("time new roman",15,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
F1.place(x = 0,y = 80,relwidth = 1)

        #===============Customer Name===========#
cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = cus_name)
cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

        #=================Customer Phone==============#
cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = c_phone)
cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

        #====================Customer Bill No==================#
cbill_lbl = Label(F1,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
cbill_lbl.grid(row = 0,column = 4,padx = 20)
cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable =c_bill_no)
cbill_en.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)
        
        #==================Food Frame=====================#
F2 = LabelFrame(root,text = 'Food',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
F2.place(x = 5,y = 180,width = 325,height = 380)

        #===========Frame Content
bath_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Bread")
bath_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
bath_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = bread)
bath_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Candy
face_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Candy")
face_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = candy)
face_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #========Hamburger
wash_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Hamburger")
wash_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = hamburger)
wash_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Hotdog
hair_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Hotdog")
hair_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = hotdog)
hair_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============Sandwich
lot_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Sandwich")
lot_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
lot_en = Entry(F2,bd = 8,relief = GROOVE,textvariable =sandwich)
lot_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Grocery Frame=====================#
F2 = LabelFrame(root,text = 'Grocery',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
F2.place(x = 330,y = 180,width = 325,height = 380)

        #===========Frame Content
rice_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Rice")
rice_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
rice_en = Entry(F2,bd = 8,relief = GROOVE,textvariable =rice)
rice_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
oil_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Food Oil")
oil_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
oil_en = Entry(F2,bd = 8,relief = GROOVE,textvariable =food_oil)
oil_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
daal_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Salt")
daal_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
daal_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = salt)
daal_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
wheat_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Wheat")
wheat_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
wheat_en = Entry(F2,bd = 8,relief = GROOVE,textvariable =wheat)
wheat_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
sugar_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Sugar")
sugar_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
sugar_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = sugar)
sugar_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Other Stuff=====================#

F2 = LabelFrame(root,text = 'Others',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
F2.place(x = 655,y = 180,width = 325,height = 380)

        #===========Frame Content
maza_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Gatorade")
maza_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
maza_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = gatorade)
maza_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
cock_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Coke")
cock_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
cock_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = coke)
cock_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
frooti_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Juice")
frooti_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
frooti_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = juice)
frooti_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
cold_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Waffer")
cold_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
cold_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = waffer)
cold_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Biscuits")
bis_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
bis_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = biscuits)
bis_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #===================Bill Aera================#
F3 = Label(root,bd = 10,relief = GROOVE)
F3.place(x = 960,y = 180,width = 325,height = 380)

#* make TreeView to display data *

#help to make capapbility of scrolling data
scroll_x=Scrollbar(F3,orient=HORIZONTAL)
scroll_y=Scrollbar(F3,orient=VERTICAL)

Supermarket_SystemList=ttk.Treeview(F3,height=12,columns=('BillNo','name','total','TotalFood','TotalGrocery','OthersTotal','FoodTax','GroceryTax','OtherTax','mobile'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

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

        #===========Buttons Frame=============#
F4 = LabelFrame(root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
F4.place(x = 0,y = 560,relwidth = 1,height = 145)

        #===================
cosm_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Food")
cosm_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
cosm_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = total_food)
cosm_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        #===================
gro_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Grocery")
gro_lbl.grid(row = 1,column = 0,padx = 10,pady = 5)
gro_en = Entry(F4,bd = 8,relief = GROOVE,textvariable =total_grocery)
gro_en.grid(row = 1,column = 1,ipady = 2,ipadx = 5)

        #================
oth_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Others Total")
oth_lbl.grid(row = 2,column = 0,padx = 10,pady = 5)
oth_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = total_other)
oth_en.grid(row = 2,column = 1,ipady = 2,ipadx = 5)

        #================
cosmt_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Food Tax")
cosmt_lbl.grid(row = 0,column = 2,padx = 30,pady = 0)
cosmt_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = tax_cos)
cosmt_en.grid(row = 0,column = 3,ipady = 2,ipadx = 5)

        #=================
grot_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Grocery Tax")
grot_lbl.grid(row = 1,column = 2,padx = 30,pady = 5)
grot_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = tax_groc)
grot_en.grid(row = 1,column = 3,ipady = 2,ipadx = 5)

        #==================
otht_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Others Tax")
otht_lbl.grid(row = 2,column = 2,padx = 10,pady = 5)
otht_en = Entry(F4,bd = 8,relief = GROOVE,textvariable =tax_other)
otht_en.grid(row = 2,column = 3,ipady = 2,ipadx = 5)

#Function to get total prices
def total():
    
        #=================Total Food Prices
    total_food_prices = (
        (bread.get() * 1)+
        (candy.get() * 3)+
        (hamburger.get() * 8)+
        (hotdog.get() * 6)+
        (sandwich.get() * 4)
        )
    total_food.set("$"+str(total_food_prices))
    tax_cos.set("$"+str(round(total_food_prices*0.05)))
        #====================Total Grocery Prices
    total_grocery_prices = (
        (wheat.get()*1)+
        (food_oil.get() * 5)+
        (salt.get() * 1)+
        (rice.get() *3)+
        (sugar.get() * 2)

        )
    total_grocery.set("$"+str(total_grocery_prices))
    tax_groc.set("$"+str(round(total_grocery_prices*0.05)))
        #======================Total Other Prices
    total_other_prices = (
            (gatorade.get() * 4)+
            (juice.get() * 2)+
            (coke.get() * 2)+
            (waffer.get() * 2)+
            (biscuits.get() * 2)
        )
    total_other.set("$"+str(total_other_prices))
    tax_other.set("$"+str(round(total_other_prices*0.05)))
    
     #======================Total
    alltotal=(total_food_prices+total_grocery_prices+ total_other_prices  ) 
    total1.set("$"+str((alltotal)))
    database()



def exitButton():
    clear=tkinter.messagebox.askyesno('Student Management System','Confirm if you want to Exit')
    if clear>0:
        root.destroy()
        return
    #====================
        
total_btn = Button(F4,text = "Total",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = total)
total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)
total_en= Entry(F4,bd = 8,relief = GROOVE,textvariable =total1)
total_en.grid(row = 1,column = 5,ipady = 2,ipadx = 5)

        #======================
exit_btn = Button(F4,text = "Exit",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command =exitButton)
exit_btn.grid(row = 1,column = 15,ipadx = 20,padx = 5)
   
        #data das
        
def database():
    Name=cus_name.get()
    Billnum=c_bill_no.get()
    TOTAL=total1.get()
    TOTAL_food=total_food.get()
    TOTAL_grocery=total_grocery.get()
    TOTAL_others=total_other.get()
    food_tax=tax_cos.get()
    grocery_tax=tax_groc.get()
    others_tax=tax_other.get()
    Mobile=c_phone.get()
   
    #===========================
    BackEnd.addCustomer(Billnum,Name,TOTAL,TOTAL_food,TOTAL_grocery,TOTAL_others,food_tax,grocery_tax,others_tax,Mobile)
    

def displayButton():
   
    result =BackEnd.Display()
    #remove tree view from other display
    Supermarket_SystemList.delete(*Supermarket_SystemList.get_children())
    for row in result:
        Supermarket_SystemList.insert('',END,values=row)
   



btnDisplay=Button(F4,font=("lucida",12,"bold"),text='Display',bg = bg_color,fg = fg_color,bd = 7,relief = GROOVE,command =displayButton)
btnDisplay.grid(row = 1,column = 7,ipadx = 20,padx = 30)
        



root.mainloop()