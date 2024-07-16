import sqlite3
def supermarketData():
    db=sqlite3.connect("Supermarket_System.db")
    cr=db.cursor()
    cr.execute("""create table if not exists supermarket
           (
            BillNo integer NOT NULL PRIMARY KEY,
            name text,
            total float,
            TotalFood float,
            TotalGrocery float,
            OthersTotal float,
            FoodTax float,
            GroceryTax float,
            OtherTax float,
            mobile text
           )""")
     
   ##################################################################
    db.commit()
    db.close()
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def Display():
    db=sqlite3.connect("Supermarket_System.db")
    cursor=db.cursor()
    data=cursor.execute('select * from supermarket')
    db.commit()
    return data
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def deletecustomer(BillNo):
    db=sqlite3.connect("Supermarket_System.db")
    cursor=db.cursor()
    cursor.execute(f'delete from supermarket where BillNo={BillNo}')
    db.commit()
    db.close()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def updateSupermarket(BillNo,name,total,TotalFood,TotalGrocery,OthersTotal,FoodTax,GroceryTax,OtherTax,mobile):
    db=sqlite3.connect("Supermarket_System.db")
    cursor=db.cursor()
    cursor.execute('update supermarket set name=? ,BillNo=?,total=?,TotalFood=?,TotalGrocery=?,OthersTotal=?,FoodTax=?,GroceryTax=?,OtherTax=?,mobile=? where BillNO=? ',(name,BillNo,total,TotalFood,TotalGrocery,OthersTotal,FoodTax,GroceryTax,OtherTax,mobile))
    db.commit()
    db.close()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def addCustomer(BillNo,name,total,TotalFood,TotalGrocery,OthersTotal,FoodTax,GroceryTax,OtherTax,mobile):
    db=sqlite3.connect("Supermarket_System.db")
    cursor=db.cursor()
    cursor.execute('insert into supermarket values (?,?,?,?,?,?,?,?,?,?)',(int(BillNo),str(name),str(total),str(TotalFood),str(TotalGrocery),str(OthersTotal),str(FoodTax),str(GroceryTax),str(OtherTax),str(mobile)))
    db.commit()
    db.close()








supermarketData()            

