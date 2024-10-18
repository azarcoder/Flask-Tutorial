from flask import Flask, render_template,flash,request
app = Flask(__name__)

app.secret_key = "123"

@app.route("/", methods = ['GET', 'POST'])
def main():
    if request.method == 'POST':
        if request.form.get('success'):
            flash('success message', 'success')
        elif request.form.get('error'):
            flash('error message', 'error') #flash(message, category) - category used for styling the message

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)