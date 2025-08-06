import re

un="Nitin7424"

un_pattern="[^A-Z]+[a-z]+[0-9$]"

x=re.findall(un_pattern, un)

if x:
    print("Valid username") 
else:
    print("Invalid username")