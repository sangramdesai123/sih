# import the Flask class from the flask module
from flask import Flask, render_template
import pyrebase
from config import *
# create the application object
app = Flask(__name__)

firebase = pyrebase.initialize_app(con)
db = firebase.database()

@app.route('/')
def home():
    return render_template('home.html')  # render a home template

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


#db.child("roadlyser").push({"author":"gole"})

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)