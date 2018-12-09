#Create a table
import sqlite3
conn=sqlite3.connect("celebrities.db")
cursor=conn.cursor()
#create a table called "celebs" with 7 fields
sql="create table celebs(celebid int PRIMARY KEY, firstname text,\
    lastname text, age int, email text, photo text, bio text)"
#create a table called "members" with 6 fields
sql2="create table members(memberid int PRIMARY KEY, firstname text,\
    lastname text, age int, email text, bio text)"
cursor.execute(sql)
cursor.execute(sql2)
#commit the changes to the database
conn.commit()
conn.close()
