import sqlite3

try:
    con = sqlite3.connect("temp.db")
    print(" database created.")
except:
    print("error!")
# creating table
"""new= " create table new(id integer primary key autoincrement, name text, age integer,city text)"
ins="insert into new(name, age, city) values(1,'nitin',21,'Keshod'),(2,'aadi',15,'rajkot'),(3,'aniruddh',20,'gondal'),(4,'dharmaraj',19,'rajkot');"
ans="insert into new(name, age, city) values(1,'nitin',21,'Keshod'),(2,'aadi',15,'rajkot'),(3,'aniruddh',20,'gondal'),(4,'dharmaraj',19,'rajkot');"

try:
    con.execute(new)
    con.execute(ins)
    con.execute(ans)
    con.commit()
    print('Data inserted Successfully.')
    
except Exception as e:
    print(e)"""

#update
"""upd= "update new set name='pratik', age=23 where id=2;"

try:
    
    con.execute(upd)
    con.commit()
    print('Data inserted Successfully.')
    
except Exception as e:
    print(e)
"""
dlt="delete from new where id=4;"


"""try:
    
    con.execute(dlt)
    con.commit()
    print('Data inserted Successfully.')
    
except Exception as e:
    print(e)"""
#show data from table
cr=con.cursor()
show="select * from new;"
try:
    
    cr.execute(show)
    data=cr.fetchall()
    #data=cr.fetchmany(2:)
    #data=cr.fetchone()
    for i in data:
        print(i)
    

    
except Exception as e:
    print(e)