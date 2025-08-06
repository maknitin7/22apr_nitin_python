import sqlite3

try:
    con = sqlite3.connect("database.db")
    print(" Database Connected.")
except:
    print("error!")

ins="insert into new(name, age, city) values('nitin',21,'Keshod'),('aadi',15,'rajkot'),('aniruddh',20,'gondal'),('dharmaraj',19,'rajkot');"

try:
    con.execute(ins)
    con.commit()
    print('Data inserted Successfully.')
except Exception as e:
    print(e)

csr=con.cursor()
show="select * from new;"
try:
    csr.execute(show)
    data=csr.fetchall()
    print("Data from database:")
    for row in data:
        print(row)

except Exception as e:
    print(e)