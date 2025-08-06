f=open("Abc.txt", "w")



choice=int(input("how many students information you want to add: "))
for i in range(choice):

    id=input("Enter your id: ")
    name=input("Enter your name: ")
    city=input("Enter your city: ")

    f.write("Id: "+id+"\n")
    f.write("Name: "+name+"\n")
    f.write("City: "+city+"\n")
    f.write("\n")
