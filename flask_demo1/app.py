#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/bootstrap')
def bootstrap():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['Username'] != 'admin' or request.form['Password'] != 'admin':
            #error = 'invalid user or password'
            pass
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
