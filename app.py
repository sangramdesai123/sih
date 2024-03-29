# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for
import pyrebase
from config import *
import requests
import os
from werkzeug import secure_filename

# create the application object
app = Flask(__name__)

firebase = pyrebase.initialize_app(con)
db = firebase.database()

@app.route('/')
def home():
    return render_template('home.html')  # render a home template

@app.route('/goog')
def goog():
	return render_template('goog.html')

@app.route('/history')
def history():
	values = list(db.get().val().values())
	print(values)	
	arr = []
	for i in range(len(values)):
		arr.append([values[i]["author"],values[i]["date"],values[i]["location"]["road"]+","+values[i]["location"]["city"],values[i]["pci"],values[i]["time"]])
	print(arr)
	return render_template('history.html',values=arr)

@app.route('/report')
def report():
	
	return render_template('report.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))


#db.child("roadlyser").push({"author":"gole"})

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)