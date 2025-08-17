import Books
import User
import Admin
import Tables
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Ishaan",database="project")
mycursor=mydb.cursor()

def BookManagement():
    while True:
        print("\t\t\t Book Record Management\n")
        print("==============================================================")
        print("1. Add Book Record")
        print("2. Display Book Records")
        print("3. Search Book Record")
        print("4. Delete Book Record")
        print("5. Update Book Record")
        print("6. Return to Main Menu")
        print("==============================================================")
        choice=int(input("Enter Choice between 1 to 6-------> : "))
        if choice==1:
            Books.insertBook()
        elif choice==2:
            Books.displayBook()
        elif choice==3:
            Books.searchBook()
        elif choice==4:
            Books.deleteBook()
        elif choice==5:
            Books.updateBook()
        elif choice==6:
            return
        else:
            print("Wrong Choice......Enter Your Choice again")
            x=input("Press Enter to continue")

            
def UserManagement():
    while True:
        print("\t\t\t User Record Management\n")
        print("==============================================================")
        print("1. Add User Record")
        print("2. Display User Records")
        print("3. Search User Record")
        print("4. Delete User Record")
        print("5. Update User Record")
        print("6. Return to Main Menu")
        print("==============================================================")
        choice=int(input("Enter Choice between 1 to 6-------> : "))
        if choice==1:
            User.insertUser()
        elif choice==2:
            User.displayUser()
        elif choice==3:
            User.searchUser()
        elif choice==4:
            User.deleteUser()
        elif choice==5:
            User.updateUser()
        elif choice==6:
            return
        else:
            print("Wrong Choice......Enter Your Choice again")
            x=input("Press Enter to continue")

            
def AdminManagement():
    while True:
        print("\t\t\t Admin Record Management\n")
        print("==============================================================")
        print("1. Add Admin Record")
        print("2. Display Admin Records")
        print("3. Search Admin Record")
        print("4. Delete Admin Record")
        print("5. Update Admin Record")
        print("6. Return to Main Menu")
        print("==============================================================")
        choice=int(input("Enter Choice between 1 to 6-------> : "))
        if choice==1:
            Admin.insertAdmin()
        elif choice==2:
            Admin.displayAdmin()
        elif choice==3:
            Admin.searchAdmin()
        elif choice==4:
            Admin.deleteAdmin()
        elif choice==5:
            Admin.updateAdmin()
        elif choice==6:
            return
        else:
            print("Wrong Choice......Enter Your Choice again")
            x=input("Press Enter to continue")

 

def BookCentre():
    while True:
        print("\t\t\t Book Centre \n")
        print("==============================================================")
        print("1. List of all Books ")
        print("2. Issue Book ")
        print("3. Display Issued Book Records ")
        print("4. Return Issued Book ")
        print("5. Return to Main Menu ")
        print("==============================================================")
        choice=int(input("Enter Choice between 1 to 5-------> : "))
        if choice==1:
            Books.BookList()
        elif choice==2:
            Books.IssueBook()
        elif choice==3:
            Books.ShowIssuedBook()
        elif choice==4:
            Books.returnBook()
        elif choice==5:
            return
        else:
            print("Wrong Choice......Enter Your Choice again")
            x=input("Press Enter to continue")

def Feedback():
    while True:
        data=()
        print("\t\t\t Feedback and Rating\n")
        print("==============================================================")
        Feedback=input("Enter your Review about our Library and tell us how can we improve :))---->")
        Ratings=input("Rate us out of 10:")
        data=(Feedback,Ratings)
        query="INSERT INTO Feedback VALUES (%s, %s)"
        mycursor.execute(query,data)
        mydb.commit()
        print()
        print("Thank you for your valuable Feedback")
        return      


