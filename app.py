from flask import Flask, render_template, request, redirect, Markup, flash
from flask_mysqldb import MySQLdb
import mysql.connector
import MySQLdb 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'DATA'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mydb = mysql.connector.connect(host="localhost",user="root",password="2580",database="amal")
        mycursor = mydb.cursor()   
        global x
        if request.form['button'] == 'forward':
            x = 'f'
            sql = "INSERT INTO sm (val) VALUES ('f')"
            mycursor.execute(sql)
            mydb.commit()
            return redirect('/users')
        elif request.form['button'] == 'right':
            x = 'r'
            sql = "INSERT INTO sm (val) VALUES ('r')"
            mycursor.execute(sql)
            mydb.commit()
            return redirect('/users')        
        elif request.form['button'] == 'left':
            x = 'l'
            sql = "INSERT INTO sm (val) VALUES ('l')"
            mycursor.execute(sql)
            mydb.commit()
            return redirect('/users')
        elif request.form['button'] == 'backward':
            x = 'b'
            sql = "INSERT INTO sm (val) VALUES ('b')"
            mycursor.execute(sql)
            mydb.commit()
            return redirect('/users')
        else:
            x = 's'
            sql = "INSERT INTO sm (val) VALUES ('s')"
            mycursor.execute(sql)
            mydb.commit()
            return redirect('/users')
    return render_template('index.html')
@app.route('/users', methods=['GET', 'POST'])
def users():
        try: 
            if x == 'f':      
                message = Markup("<h1>f</h1>")
                flash(message)    
            elif x == 'l':
                message = Markup("<h1>l</h1>")
                flash(message)
            elif x == 'r':
                message = Markup("<h1>r</h1>")
                flash(message)
            elif x == 'b':
                message = Markup("<h1>b</h1>")
                flash(message)
            else:
                message = Markup("<h1>s</h1>")
                flash(message)
        except MySQLdb._exceptions.ProgrammingError  as e :{} 
        except MySQLdb._exceptions.OperationalError  as e :{}       
        return render_template('users.html')
if __name__ == '__main__':
    app.run(debug=True)
 