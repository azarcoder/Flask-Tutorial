from flask import Flask, render_template, request, flash
import os
import pandas as pd

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/csv'
app.secret_key = "123"

@app.route("/", methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        myfile = request.files['mycsvfile']
        if myfile!='':
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], myfile.filename)
            myfile.save(filepath)

            data = pd.read_excel(myfile)
            return render_template('view.html', data = data.to_html(index=False).replace('<th>', '<th style = "text-align : center ">')) 
    return render_template('uploadcsv.html')

if __name__ == "__main__":  
    app.run(debug=True)