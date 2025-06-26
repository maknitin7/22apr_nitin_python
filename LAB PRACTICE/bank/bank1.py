import random
import bank2
while True:

        print("Press 1 for continue and 2 for exit")
        cont = int(input("Enter your choice: "))
        if cont == 2:
            print("Thanks for visiting")
            break
        elif cont != 1:
            print("Invalid choice, please try again.")
            continue
        else:
            print("press \n 1 for account opening \n 2 for deposit \n 3 for withdrawal \n 4 for statement \n 5 for exit  \n press 6 for viewing all accounts \n First press 1 then only open statement")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                
                bank2.open_account()
            elif choice == 2:
                bank2.deposit()
            elif choice == 3:
                bank2.withdrawal()
            elif choice == 4:
                bank2.statement()
            elif choice == 5:
                print("Thanks for visiting")
                break
            elif choice == 6:
                bank2.view_all_accounts()
                
            else:
                print("Error")
                break

