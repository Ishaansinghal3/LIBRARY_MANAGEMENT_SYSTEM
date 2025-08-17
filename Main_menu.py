import Operations
def Adminmenu() :
    while True:
        print("\t\t\t Admin Menu \n")
        print("==============================================================")
        print("1. Book Management")
        print("2. User Management")
        print("3. Admin management")
        print("4. Logout ")
        print("==============================================================")
        choice=int(input("Enter Choice between 1 to 4-------> : "))
        if choice==1:
            Operations.BookManagement()
        elif choice==2:
            Operations.UserManagement()
        elif choice==3:
            Operations.AdminManagement()
        elif choice==4:
            print("Thanks for visiting our Library:))")
            print("Logged out of the system")
            break
        else:
            print("Wrong Choice......Enter Your Choice again")
            continue
    

def Usermenu() :
    while True:
        print("\t\t\t User Menu \n")
        print("==============================================================")
        print("1. Book Centre")
        print("2. Feedback and Ratings")
        print("3. Logout ")
        print("==============================================================")
        choice=int(input("Enter Choice between 1 to 3-------> : "))
        if choice==1:
            Operations.BookCentre()
        elif choice==2:
            Operations.Feedback()
        elif choice==3:
            print("Thanks for visiting our Library:))")
            print("Logged out of the system")
            break
        else:
            print("Wrong Choice......Enter Your Choice again")
            continue
   
