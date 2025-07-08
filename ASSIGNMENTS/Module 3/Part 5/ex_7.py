def calc():
    
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        choice= input("Enter operation: (1 for sum, 2 for subtraction, 3 for multiplication, 4 for division: )")

        if choice == '1':
            sum = a + b
            print("Sum:", sum)
        elif choice == '2':
            sub = a - b
            print("Subtraction:", sub)
        elif choice == '3':
            mul = a * b
            print("Multiplication:", mul)
        elif choice == '4':
            try:
                div = a / b
                print("Division:", div)
            except :
                print("Division by zero is not allowed.")
        else:
            print("Invalid operation.")

calc()