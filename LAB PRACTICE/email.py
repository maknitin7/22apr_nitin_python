import re

email=input("enter your email: ")
email_pattern="[a-z]+\W+[0-9]"
x=re.findall(email_pattern, email)

if x:
    print("Valid email")
else:
    print("Invalid email")
    