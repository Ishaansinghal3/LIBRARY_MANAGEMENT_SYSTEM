import sys
import Main_menu
import Tables
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Ishaan", database="project")
mycursor = mydb.cursor()

def create_admin_account():
    print("CREATE ADMIN ACCOUNT")
    AdminID = input("Enter new Admin ID: ")
    Password = input("Enter Password to be set: ")

    data = (AdminID, Password)
    query = "INSERT INTO AdminRecord (AdminID, Password) VALUES (%s, %s)"
    mycursor.execute(query, data)
    mydb.commit()

    mycursor.execute("SELECT AdminID FROM AdminRecord WHERE AdminID = %s", (AdminID,))
    result = mycursor.fetchone()

    if result:
        print("Admin account successfully created")
    else:
        print("Account creation failed or admin already exists")

def login_to_admin():
    print("\n")
    print("  T  H  E    B  O  O  K    W  O  R  M  ")
    print()
    print("1. CREATE ADMIN ACCOUNT")
    print("2. LOGIN TO YOUR ACCOUNT")
    ch = int(input("Enter choice--> "))
    
    if ch == 1:
        create_admin_account()
        print("\nPlease log in to your account.")
        ch = 2

    if ch == 2:
        print("WARNING: Only three attempts to login at a time")
        for attempts in range(0, 3):
            AdminID = input("\t  Enter AdminID : ")
            password = input("\t  Enter Password : ")

            print()
            mycursor.execute("SELECT Password FROM AdminRecord WHERE AdminID = %s", (AdminID,))
            result = mycursor.fetchone()

            if result:
                temp, = result
                if temp == password:
                    print(f"\n\t\t    WELCOME {AdminID} to THE BOOK WORM  \n ")
                    Main_menu.Adminmenu()
                    break
                else:
                    print("\t INVALID PASSWORD OR USERNAME! TRY AGAIN ")
                    print(f"\t {attempts + 1} attempt is over \n")
            else:
                print("\t NO SUCH USERNAME! TRY AGAIN ")
                print(f"\t {attempts + 1} attempt is over \n")
    else:
        print("Enter valid choice")
        login_to_admin()

def login_to_user():
    print("\n")
    print(" T  H  E    B  O  O  K    W  O  R  M  ")
    print()
    print("1.CREATE ACCOUNT")
    print("2.LOGIN TO YOUR ACCOUNT")
    
    ch = int(input("Enter choice--> "))
    
    if ch == 1:
        UserId = input("Enter your UserId: ")
        UserName = input("Enter your Name: ")
        Password = input("Enter Password to be set: ")
        
        data = (UserId, UserName, Password, None)
        query = "INSERT INTO UserRecord VALUES (%s, %s, %s, %s)"
        mycursor.execute(query, data)
        mydb.commit()
        
        mycursor.execute("SELECT UserId FROM UserRecord WHERE UserId = %s", (UserId,))
        result = mycursor.fetchone()
        
        if result:
            print("Account successfully created")
        else:
            print("Account already exists")
        
        print("\nPlease log in to your account.")
        ch = 2

    if ch == 2:
        print("WARNING: Only three attempts to login at a time")
        
        for attempts in range(0, 3):
            UserID = input("\t  Enter UserID : ")
            password = input("\t  Enter Password : ")
            
            print()
            mycursor.execute("SELECT Password FROM UserRecord WHERE UserID = %s", (UserID,))
            result = mycursor.fetchone()
            
            if result:
                temp, = result
                if temp == password:
                    print(f"\n\t\t    WELCOME {UserID} to THE BOOK WORM  \n ")
                    Main_menu.Usermenu()
                    break
                else:
                    print("\t INVALID PASSWORD OR USERNAME! TRY AGAIN ")
                    print(f"\t {attempts + 1} attempt is over \n")
            else:
                print("\t NO SUCH USERNAME! TRY AGAIN ")
                print(f"\t {attempts + 1} attempt is over \n")
    else:
        print("Enter valid choice")
        login_to_user()

def menu():
    while True:
        print("\n\n")
        print(" T  H  E    B  O  O  K    W  O  R  M  ")
        print("\n")
        print(" ==== MENU ====\n")
        print(" 1. Login as an ADMIN")
        print(" 2. Login as a USER")
        print(" 3. EXIT \n\n ")

        ch = input(" Select [ 1/2/3 ] : ")
        print()
        
        if ch == "1":
            login_to_admin()
        elif ch == "2":
            login_to_user()
        elif ch == "3":
            cancel_request = input(" DO YOU WISH TO EXIT... [yes/no ] :  ")
            if cancel_request.lower() == "yes":
                print("Exiting the system.")
                sys.exit()
        else:
            print(" INVALID COMMAND ")
            print(" RETRY \n")

menu()
