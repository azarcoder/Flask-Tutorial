from flask import Flask, render_template, request, flash
import os
app = Flask(__name__)
app.secret_key = "123"

app.config['UPLOAD_FOLDER1'] = "static/pdf"
app.config['UPLOAD_FOLDER2'] = "static/csv"
app.config['UPLOAD_FOLDER3'] = "static/videos"

# Ensure the directories exist
os.makedirs(app.config['UPLOAD_FOLDER1'], exist_ok=True)
os.makedirs(app.config['UPLOAD_FOLDER2'], exist_ok=True)
os.makedirs(app.config['UPLOAD_FOLDER3'], exist_ok=True)

@app.route("/", methods = ['GET', 'POST'])
def main():
    if request.method == 'POST':
        pdf_file = request.files['upload_pdf'] #used to get filname 
        csv_file = request.files['upload_csv']
        vid_file = request.files['upload_vid']

        try:        
            if pdf_file!='' and csv_file!='' and vid_file!='':
                filepath1 = os.path.join(app.config['UPLOAD_FOLDER1'], pdf_file.filename)
                filepath2 = os.path.join(app.config['UPLOAD_FOLDER2'], csv_file.filename)
                filepath3 = os.path.join(app.config['UPLOAD_FOLDER3'], vid_file.filename)

                pdf_file.save(filepath1)
                csv_file.save(filepath2)
                vid_file.save(filepath3)

                flash('Files uploaded Successfully', 'success')
        except FileNotFoundError as e:
             flash(e, 'error')

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)