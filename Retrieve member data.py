#Retrieve Data
import sqlite3
conn=sqlite3.connect("celebrities.db")
cursor=conn.cursor()
#SQL SELECT statement

sql2="select * from members"
cursor.execute(sql2)

#get the rows
rows=cursor.fetchall()
#iterate over the results and print them
for row in rows:
    print(row)
conn.close()
