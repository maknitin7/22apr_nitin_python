import random
import datetime
f=open("Abc.txt", "a")



choice=int(input("how many students information you want to add: "))
for i in range(choice):

    id=random.randint(100, 999)
    x=str(id)
    name=input("Enter your name: ")
    city=input("Enter your city: ")
    
    f.write("created at: "+str(datetime.datetime.now())+"\n")
    f.write("Id: "+x+"\n")
    f.write("Name: "+name+"\n")
    f.write("City: "+city+"\n")
    f.write("---------------------------------")
    f.write("\n")
