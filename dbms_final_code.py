import random
import mysql.connector
mydb  = mysql.connector.connect(host = "127.0.0.1",user = "root" , passwd = "kritika_21395#", auth_plugin='mysql_native_password')

mycursor = mydb.cursor()
mycursor.execute("use call_a_cab")

#Define the function for creating a new account
def create_account():
    Email = input("Enter your Email: ")
    Password = input("Create password: ")
    Name= input("Enter your Name: ")
    Location= input("Enter your location: ")

    # Check if the email already exists
    mycursor.execute("SELECT * FROM passenger_account WHERE Email=%s", (Email,))
    existing_user = mycursor.fetchone()

    if existing_user:
        print("\nUser already exists...move to Login")
    else:
        # Add the new user to the database
        sql = "INSERT INTO passenger_account (Passenger_ID,Email, Password, Name, Location) VALUES (%s,%s, %s, %s, %s)"
        val = (None,Email, Password, Name, Location)
        mycursor.execute(sql, val)
        mydb.commit()
        print("\nAccount created successfully") 

def book_ride():
    print("\nRequest Ride!")
    p_ID= int(input("Enter your ID: "))
    pickup= input("pickup location: ")
    dropoff= input("Enter dropoff location: ")
    amount= random.randint(1,5000)
    print("\nEstimated Ride Amount= ", amount)
    input("Type 'enter' to proceed: ")

    # Insert the ride request information into the database
    sql = "INSERT INTO ride_request (Request_ID,Pickup_location, Dropoff_location, Passenger_ID) VALUES (%s,%s,%s,%s)"
    val = (None,pickup, dropoff,p_ID)
    mycursor.execute(sql, val)
    mydb.commit()
    
    print("\nRide Requested...looking for drivers")
    print("------------------------------------------------------")
    print("\nDriver is on the way")

    mycursor.execute("SELECT Driver_ID, Mobile_No, Rating FROM driver WHERE Rating IN (3,4,5) AND Status='Available'")
    result= mycursor.fetchall()
    for i in result:
        print("Driver ID: ",i[0])
        print("Mobile No.: ",i[1])
        print("Rating: ",i[2])
    
    request_ID= mycursor.execute("SELECT Request_ID FROM ride_request WHERE Passenger_ID="+str(p_ID))
    
    ride= input("\ntype 'enter to start ride: ")
    if ride== "enter":
        print("Ride ongoing.........")
        # Insert the ride information into the database
        sql = "INSERT INTO ride (Ride_ID,Pickup_location, Dropoff_location, Request_ID) VALUES (%s,%s,%s,%s)"
        val = (None,pickup, dropoff,request_ID)
        mycursor.execute(sql, val)
        mydb.commit()
    
    print("-----------------------------------------------------")
    print("\nRide Completed...proceed to make payment")
    mode= input("\nEnter payment mode: ")
    payment= input("press enter to make payment: ")
    if payment== "enter":
        # Insert the payment information into the database
        sql = "INSERT INTO payments (Ride_ID,Amount, Payment_Mode, Passenger_ID) VALUES (%s,%s,%s,%s)"
        val = (None,amount, mode,p_ID)
        mycursor.execute(sql, val)
        mydb.commit()
        print("\n Payment Successful! Thanks for riding with us!")
        print("--------------------------------------------------------------------")   
    else:
        print("Payment Failed, try again!") 
    
def view_account_details(Email, Password):
    # Retrieve account details from the database
    mycursor.execute("SELECT * FROM passenger_account WHERE Email=%s AND Password=%s", (Email, Password))
    result = mycursor.fetchall()
    print("\nYour Account Details\n")
    for i in result:
        print("ID: ",i[0])
        print("Email: ",i[1])
        print("Password: ",i[2])
        print("Name: ",i[3])
        print("Location: ",i[4])
        
    delete= input("\nPress D to delete this account, else press P to proceed: ")
    if delete=="D":
        mycursor.execute("DELETE FROM passenger_account WHERE Email= %s",(Email,))
        print("Account Deleted")
    if delete=="P":
        pass

#Define the function for logging into existing account
def login():
    Email = input("Enter your Email: ")
    Password = input("Enter password: ")

     # Check if the email and password are correct
    mycursor.execute("SELECT * FROM passenger_account WHERE Email=%s AND Password=%s", (Email, Password))
    existing_user = mycursor.fetchone()

    if existing_user:
        print("\nLogin Successful!")
        print("\nWelcome!!")
        while True:
            print("\n1. Book a Ride")
            print("2. View Account Details")
            print("3. Return")
            main= int(input("Your choice is: "))
            if main==1:
                book_ride()
            if main==2:
                view_account_details(Email, Password)
            if main==3:
                break

    else:
        print("\nIncorrect email or password")

while True:  
    print("\nEnter your Choice:")  
    print("1. Create a New Account")  
    print("2. Login Account")  
    print("3. Exit")
    select_choice = int(input("\nYour Choice is: "))

    if select_choice==1:
        create_account()
    if select_choice==2:
        login()
    if select_choice==3:
        break

