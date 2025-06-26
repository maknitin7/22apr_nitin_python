import random
account=[]
a= "a"
b="a"
c="a"
d=0

def open_account():
    global a,b,c,d
    account.append((a, b, c, d))
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

def view_all_accounts():
    account.append((a, b, c, d))
    account.pop(0)
    print("-----ACCOUNT DETAILS -----  \n")

    for i in account:
                    
                    print("Account Name:", i[0])
                    print("Account Type:", i[1])
                    print("Account Number:", i[2])
                    print("Balance:", i[3])
                    print("---------------------------")
                
