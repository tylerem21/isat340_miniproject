#Insert Multiple Rows
import sqlite3
conn=sqlite3.connect("celebrities.db")
cursor=conn.cursor()
#data supplied as tuple of tuples
sql="insert into celebs values (?,?,?,?,?,?,?)"
data=((1, "Angelina", "Jolie", 40, "angie@hollywood.us","http://www.nphinity.com/pics/aj.jpg", "Angelina \
Jolie is an American actress, \
filmmaker, and humanitarian. She has received an Academy Award, two Screen Actors Guild \
Awards, and three Golden Globe Awards, and has been cited as Hollywood's highest-paid \
actress. "),(2, "Brad", "Pitt", 51, "brad@hollywood.us", "http://www.nphinity.com/pics/bp.jpg", "William \
Bradley Pitt is an American actor and film producer. He has received \
multiple awards and nominations including an Academy Award as producer under his own company \
Plan B Entertainment."),(3,"Snow","White",21,"sw@disney.org","http://www.nphinity.com/pics/sw.jpg","Snow White \
is a 19th-century German fairy tale which is today known widely across the Western world. The Brothers \
Grimm published it in 1812 in the first \
edition of their collection Grimms' Fairy Tales. It was titled in German: Sneewittchen \
(in modern orthography Schneewittchen) and numbered as Tale 53. The name Sneewittchen was Low \
German and in the first version it was translated with Schneeweißchen. The Grimms completed \
their final revision of the story in 1854."),(4,"Darth","Vader",29,"dv@darkside.me","http://www.nphinity.com/pics/dv.jpg\
","Darth Vader (also known as Anakin Skywalker) is a \
fictional character in the Star Wars franchise. He is the overarching central character of the\
original film series, appearing as a main and pivotal antagonist serving the Galactic Empire, \
and in the prequel trilogy as a main protagonist whose fall to the dark side of the Force \
forms the central story arc of those films. "),(5,"Taylor","Swift",25,"ts@1989.us","http://www.nphinity.com/pics/ts.jpg\
","Taylor Alison Swift is an American singer-songwriter. One of the world's leading contemporary recording \
artists, she is known for narrative songs about her personal life, which have received widespread media \
coverage."),(6,"Beyonce","Knowles",34,"beyonce@jayz.me","http://www.nphinity.com/pics/bk.jpg\
","Beyoncé Giselle Knowles-Carter is an American singer, songwriter, producer, and actress. Born and raised in \
Houston, Texas, Beyoncé performed in various singing and dancing competitions as a child. She rose to fame \
in the late 1990s as lead singer of the R&B girl-group Destiny's Child."),(7,"Selena","Gomez",23,"selena@hollywood.us\
","http://www.nphinity.com/pics/sg.jpg","Selena Marie Gomez is an American singer, actress, and producer. \
After appearing on the children's television series Barney & Friends, she received wider recognition for her \
portrayal of Alex Russo on the Disney Channel television series Wizards of Waverly Place, which aired for \
four seasons from 2007 until 2012."),(8,"Stephen","Curry",27,"steph@golden.bb","http://www.nphinity.com/pics/sc.jpg\
","Wardell Stephen Curry II is an American professional basketball player for the Golden State Warriors of the \
National Basketball Association. Many players and analysts have called him the greatest shooter in \
NBA history."))
cursor.executemany(sql,data)
#commit the changes
conn.commit()
conn.close()

