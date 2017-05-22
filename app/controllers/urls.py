# -*- coding: utf-8 -*-

from flask import render_template
from app import app

from app.models.forms import LoginForm

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('Username: %s' % form.username.data)
        print('Password: %s' % form.password.data)

    return render_template('login.html',
                           form = form)

@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')
