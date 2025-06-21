no1=int(input("Enter first number 1: "))
no2=int(input("Enter second number 2: "))

def sum():
    print("Sum:",no1+no2)
def sub():
    print("Subtraction:",no1-no2)
def mul():
    print("Multiplication:",no1*no2)
def div():
    if no2 != 0:
        print("Division:",no1/no2)
    else:
        print("Can't divide by zero")

x=input("Press 1 for sum, 2 for sub, 3 for mul, 4 for div: ")

if x == '1':
    sum()
elif x == '2':
    sub()
elif x == '3':
    mul()
elif x == '4':
    div()
else:
    print("Invalid choice")