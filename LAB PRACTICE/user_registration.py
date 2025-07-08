user=open("user.txt", "x")
try:
    name= str(input("Enter your name: "))
    if name.isupper():
        pass
    else:
        print("Name must be in uppercase")
    email= str(input("Enter your email: "))
    if email.islower():
        pass
    else:
        print("Email must be in lowercase")
    try:
        mobile=int(input("Enter your mobile number: "))
        if len(str(mobile)) == 10:
            pass
        else:
            print("Mobile number must be 10 digits")
    except :
        print("Invalid mobile number")
    password= str(input("Enter your password: "))
    if password == password.capitalize():
        if password.isalnum():
            pass
    
        
    else:
        print("Password must be alphanumeric and start with a capital letter")
    conpassword= str(input("Enter your confirm password: "))
    if conpassword == password:
        print("Registration successful")
    else:
        print("Password does not match")
except Exception as e:
    print(e)
else:
    user=open("user.txt", "a")
    #user.write("Created at:", str(datetime.datetime.now()))
    user.write(f"name:{name}\n email:{email}\n mobile:{mobile}\n password:{password}\n")