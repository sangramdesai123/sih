# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  # render a home template

@app.route('/history')
def history():
    return render_template('history.html')  # render a history template

@app.route('/report')
def report():
    return render_template('report.html')  # render a  report template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)