from flask import Flask, render_template, request, flash, session, url_for , g, redirect

#g means global request variable 
#NOTE: g is comes form Flask so never use any other name instead of g 

app = Flask(__name__)
app.secret_key = "123"

class User:
    def __init__(self, id,username,password):
        self.id = id
        self.username = username
        self.password = password 

users = []

users.append(User(id=1, username='Azar', password='123'))
users.append(User(id=2, username='duck', password='123'))


        

@app.route('/',methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['uname']
        upass = request.form['upass']
        for data in users:
            if data.username == uname and data.password == upass:
                session['user_id'] = data.id
                g.record = 1 
                return redirect(url_for('user'))
            else:
                g.record = 0
        
        if g.record == 0:
            flash("Username or Password mismatch!", 'error')
            return redirect(url_for('login'))

    return render_template('login.html')


#this will execute when you going into user panel
@app.before_request
def before_request():
    if 'user_id' in session:
        for data in users:
            if data.id == session['user_id']:
                g.user = data 
                break

@app.route('/user', methods = ['GET', 'POST'])
def user():
    if not g.user:
        return redirect(url_for('login'))
    
    return render_template('user_panel.html', )

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
    

if __name__ == "__main__":
    app.run(debug = True)