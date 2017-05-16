#! /usr/bin/env python

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } 
    posts = [
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index_base.html",
        title = 'Home',
        user = user,
        posts=posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
