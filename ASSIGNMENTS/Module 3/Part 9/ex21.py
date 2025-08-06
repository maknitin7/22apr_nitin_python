import sqlite3

try:
    con = sqlite3.connect("database.db")
    print(" Database Created.")
except:
    print("error!")

new= " create table new(id integer primary key autoincrement, name text, age integer,city text)"

try:
    con.execute(new)
    con.commit()
    print('Table created Successfully.')
    
except Exception as e:
    print(e)