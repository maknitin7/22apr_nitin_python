import sqlite3
try:
    con = sqlite3.connect("register.db")
    print(" Database Ceated.")
except:
    print("error!")
# creating table
new= " create table new(id integer primary key autoincrement, name text,city text)"
#con.execute(new)
try:
    

    while True:
        choice=int(input("Enter 1 to update, 2 to delete,3 to insert,enter any other number to exit: "))
        if choice == 1:
            upd=int(input("Enter id to update: "))
            name=input("Enter new name: ")
            city=input("Enter new city: ")
            upd=f"update new set name='{name}',city='{city}' where id={upd};"
            con.execute(upd)
            con.commit()
            print('Data updated Successfully.')
        elif choice == 2:
            delete=int(input("Enter id to delete: "))
            del_query=f"delete from new where id={delete};"
            con.execute(del_query)
            con.commit()
            print('Data deleted Successfully.')
        elif choice == 3:
            n=int(input("Enter number of records: "))

            for i in range(n):
                name=input("Enter name: ")
                city=input("Enter city: ")
                stinfo=(f"insert into new(name,city) values('{name}','{city}');")
                con.execute(stinfo)
                con.commit()
                print('Data inserted Successfully.')


        else:
            print("Invalid choice!")
            break

except Exception as e:
    print(e)