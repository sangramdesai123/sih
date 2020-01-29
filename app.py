# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  # render a template

@app.route('/history')
def home():
    return render_template('history.html')  # render a template

@app.route('/report')
def home():
    return render_template('report.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)