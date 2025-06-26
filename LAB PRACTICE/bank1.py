import random
account = []
a= "a"
b="a"
c="a"
d=0
def bank():
    
    

    while True:
        def open_account():
            global a,b,c,d
            a = input("Enter your name: ")
            b = input("Enter the type of account: ")
            c = random.randint(100000000000, 999999999999)
            print("Your account number is:", c)
            d=0
            
            

        def deposit():
            global d
            depo = int(input("Enter the amount of deposit: "))
            if depo < 2000:
                print("Minimum 2000 amount is required")
                
            else:
                print("Successfully deposited")
                d += depo
                

        def withdrawal():
            global d
            withdraw = int(input("Enter amount you want to withdraw: "))
            if withdraw > d:
                print("Error: you cannot withdraw more than your deposit")
            else:
                print("Successfully withdrawn")
                d -= withdraw
                

        def statement():
            global a, b, c, d
            print("Your account name is:", a)
            print("Your account type is:", b)
            print("Your account number is:", c)
            print("Balance:", d)

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
                account.append((a, b, c, d))
                open_account()
            elif choice == 2:
                deposit()
            elif choice == 3:
                withdrawal()
            elif choice == 4:
                statement()
            elif choice == 5:
                print("Thanks for visiting")
                break
            elif choice == 6:
                account.append((a, b, c, d))
                account.pop(0)
                print("-----ACCOUNT DETAILS -----  \n")

                for i in account:
                    
                    print("Account Name:", i[0])
                    print("Account Type:", i[1])
                    print("Account Number:", i[2])
                    print("Balance:", i[3])
                    print("---------------------------")
                
                
            else:
                print("Error")
                break

bank()