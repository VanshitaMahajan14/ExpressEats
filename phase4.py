import csv
import os
import random
import mysql.connector
mydb = mysql.connector.connect(
    user='root', password='{1}', host='localhost', auth_plugin='mysql_native_password')
cursor = mydb.cursor()
print('sql-python connection status :', mydb.is_connected())
cursor.execute("use team_34")

def option1():
    try:
        # Takes emplyee details as input
        print("Enter new customer's details: ")
        
        name = input("Name: ")
        cust_id = str(random.randint(1,99999))
        fav = input("Fav_cuisine: ")
        email= input("Email id: ")
        add = input("Address: ")
        pn= input("phone number :")
        cursor.execute("INSERT INTO customer VALUES ('{}','{}','{}','{}')".format(name,cust_id,fav,"NULL"))
        cursor.execute("INSERT INTO contact VALUES ('{}','{}','{}')".format(cust_id,email,pn))
        cursor.execute("INSERT INTO location VALUES ('{}','{}')".format(cust_id,add))
        mydb.commit()

        print("Inserted Into Database")

    except Exception as e:
        mydb.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def option2():   #show restaurants
    try:
        row = {}
        print("Enter your location: ")
        
        row["Outlet"] = input("Outlet: ")
        query = "Select * from Restaurant where Outlet = '%s' " % row["Outlet"]
        
         
       
        cursor.execute(query)
        
        
        data = cursor.fetchall()
        
       
        for row in data:
            print("Restaurant:  ",row[0],"    Headchef:",row[2],"     Timings:",row[4])
        mydb.commit()
    except Exception as e:
        mydb.rollback()
        print("Failed to display into database")
        print(">>>>>>>>>>>>>", e)

    return

def option3():   #make reservation
    try:
        row = {}
        print("Enter details of reservation:")

        row["RID"] = random.randint(0,999999)
        row["Cust_ID"] = input("Cust_ID: ")        
        row["Outlet"] = input("Outlet: ")
        row["Number_of_people"] = input("Number of people: ")
        t=int(input("Time:(hour number in 24hr clock time: "))
        row["Timing"] = str(t)
        print(row["Timing"])

        query = "INSERT INTO Reservation(RID, Outlet, Cust_ID ,Number_of_people, Timing) VALUES('%s', '%s', '%s','%s',%s)" % (
            row["RID"],row["Outlet"], row["Cust_ID"], row["Number_of_people"],row["Timing"])


        #print(query)
        cursor.execute(query)
        mydb.commit()


    except Exception as e:
        mydb.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def option4():   #fire delivery guy
    try:
        row = {}
        a = int(input("Enter order ID of order to be cancelled : "))

        query = "DELETE FROM orders where Order_ID = %s" % (a)
        #print(query)
        cursor.execute(query)
        mydb.commit()


    except Exception as e:
        mydb.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def option5():   #display order details of a customer
    try:
        row = {}
        a = (input("Enter ID of Customer: "))
        query = "SELECT * FROM Orders where Cust_ID = %s " % (a)  
        cursor.execute(query)
        data = cursor.fetchall()
        for row in data:
            print("Order_ID",row[0],"    Customer Id :",row[1],"  Status:" ,row[3])
        mydb.commit()


    except Exception as e:
        mydb.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def option8():   #display order details of a customer
    try:
        row = {}
        a = int((input("Enter ID of delivery personnel: ")))
        query = "SELECT * FROM delivery_staff where ID = %s " % (a)  
        cursor.execute(query)
        data = cursor.fetchall()
        mydb.commit()
        for row in data:
            if(row[6] == 'Free'):
                query = "delete FROM delivery_staff where ID = %s " % (a)
                cursor.execute(query)
                mydb.commit()
            else:
                print("the staff is currently delivering an order");


    except Exception as e:
        mydb.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def option7():   #display order details of a customer
    try:
        row = {}
        a = (input("Enter ID of Customer: "))
        query = "SELECT * FROM items where order_ID in (select order_ID from Orders where Cust_ID = %s )" % (a)  
        cursor.execute(query)
        data = cursor.fetchall()
        for row in data:
            print("Order ID: ",row[0],"   Items: ",row[1])
        mydb.commit()


    except Exception as e:
        mydb.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def option6():   #display order details of a customer

    try:
        
        query = "SELECT * FROM delivery_staff where Status = 'Free'"  
        cursor.execute(query)
        data = cursor.fetchall()
        for row in data:
            print("name",row[0],"    ID :",row[1],"  Location" ,row[3] , "   Phone no :",row[5])
        mydb.commit()


    except Exception as e:
        mydb.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        option1()
    elif(ch == 2):
        option2()
    elif(ch == 3):
        option3()
    elif(ch == 4):
        option4()
    elif(ch == 5):
        option5()
    elif(ch == 6):
        option6()
    elif(ch == 7):
        option7()
    elif(ch == 8):
        option8()
    else:
        print("Error: Invalid Option")

while(1):
                
                # Here taking example of Employee Mini-world
                print("1. Add a new customer")  # insert
                print("2. Display Restaurants")  # display
                print("3. Make a Reservation")  # insert
                print("4. Cancel order")  # delete
                print("5. Display Order details for a particular customer") #display
                print("6. List free delivery personnel") #display
                print("7. Look for past order items")    #display
                print("8. Fire a delivery personnel")   #delete
                print("9. Logout")
                ch = int(input("Enter choice> "))
                if ch == 9:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")
