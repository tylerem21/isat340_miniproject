#Update Data
import sqlite3
conn=sqlite3.connect("celebrities.db")
cursor=conn.cursor()
#SQL SELECT statement
sql='''update celebs set photo=replace(photo,'nphinity','software4rfid')'''
cursor.execute(sql)
#commit the changes
conn.commit()
conn.close()