import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
#insert multiple rows
sql2 = "insert into members values(?,?,?,?,?,?)"
data = ((1,"Erica","Wilder",20,"wilderea@dukes.jmu.edu\
","From Fairfax, VA"),(2,"Ethan","Tyler",21,"tylerem@dukes.jmu.edu","From Leesburg, Va."))
cursor.executemany(sql2, data)
#commit changes
conn.commit()
conn.close()
