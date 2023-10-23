from turtle import title
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html', title="Flask")
    
@app.route('/first')
def first():
    return render_template('first.html')
    
@app.route('/second')
def second():
    return render_template('second.html')


app.run()
