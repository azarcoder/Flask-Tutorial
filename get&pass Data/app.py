from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/") 
def index():
    return render_template("index.html")

@app.route('/Register', methods = ['POST','GET'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        address = request.form.get('address')
        contact = request.form.get('contact')
        return render_template('result.html', name = name, age = age, address = address, contact = contact)

if __name__ == "__main__":
    app.run(debug=True) #autorun based on save