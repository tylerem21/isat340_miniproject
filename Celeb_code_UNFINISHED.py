import sqlite3

from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    celebID = ''
    firstname = ''
    lastname = ''
    age = None
    email = ''
    photo = ''
    bio = ''

    if request.method == 'GET':

        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM users''')
        row = c.fetchone()
        print(row)

        if row:
            celebID = row[0]
            firstname = row[1]
            lastname = row[2]
            age = row[3]
            email = row[4]
            photo = row[5]
            bio = row[6]

        conn.close()

    if request.method == 'POST':
    
        name = request.form['name']
        age = request.form['age']
        photo = request.form['photo']
        bio = request.form['bio']
    
        conn = sqlite3.connect('main.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM users''')
        row = c.fetchone()
        if row:
            c.execute('''UPDATE users SET name = ?, age = ?, photo = ?, bio = ?''',
                (name, age, photo, bio))
                
        else:
            c.execute('''INSERT INTO users VALUES (?, ?, ?, ?)''',
                (name, age, photo, bio))
        conn.commit()
        conn.close()
    return render_template('my_info.htm', name=name, age=age, photo=photo, bio=bio)

def get(request):
	pass

def post(request):
	pass


	
if __name__ == '__main__':

    app.run(debug=False)
