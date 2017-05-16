#! /usr/bin/env python

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } 
    return render_template("if.html",
        user = user)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
