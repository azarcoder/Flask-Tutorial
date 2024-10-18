from flask import Flask, render_template, request, flash, redirect, url_for

import sqlite3


app = Flask(__name__)

app.secret_key = "123"

con = sqlite3.connect("database.db")
con.execute("CREATE TABLE IF NOT EXISTS data(pid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, contact INTEGER, mail TEXT)")
con.close()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/addData", methods = ['GET', 'POST'])
def addData():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            contact = request.form['contact']
            con = sqlite3.connect("database.db")
            cursor = con.cursor()

            cursor.execute("INSERT INTO data (name,contact,mail) values(?,?,?)", (name, contact, email))
            con.commit()
            con.close()
            flash('Added successfully', 'success')
        except Exception as e:
            con.rollback()  # Roll back in case of error
            flash('Error while registration: {}'.format(e), 'error')
        finally:
            return redirect(url_for("index")) #here index is a function name


@app.route('/view')
def view():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row #to show data in table    
    cur = con.cursor()
    cur.execute("SELECT * FROM data")
    data = cur.fetchall()
    con.close()
    return render_template('view.html', data = data) 

@app.route("/update/<string:id>", methods = ['POST', 'GET'])
def update(id):
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row #to show data in table    
    cur = con.cursor()
    cur.execute("SELECT * FROM data WHERE pid = ?", (id,))
    data = cur.fetchone()
    con.close()

    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            contact = request.form['contact']
            con = sqlite3.connect("database.db")
            cursor = con.cursor()
            cursor.execute("UPDATE data SET name=?, contact = ?, mail=? WHERE pid = ?", (name,contact,email,id))
            con.commit()
            flash('updated!', 'success')
        except:
            flash('Error in update', 'error')
        finally:
            con.close()
            return redirect(url_for('index'))

    return render_template('update.html', data = data)

@app.route("/delete/<string:id>", methods = ['POST', 'GET'])
def delete(id):
    try:
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("DELETE FROM data WHERE pid = ?", (id,))
        con.commit()
        flash('deleted successfully!', 'success')
    except:
        flash('Error in deletion', 'error')
    finally:
        con.close()
        return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(debug=True)
