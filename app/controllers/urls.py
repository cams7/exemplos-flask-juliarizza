# -*- coding: utf-8 -*-

from flask import redirect, url_for, render_template, flash
from flask_login import login_user, logout_user
from app import app, lm
from app.models.tables import User
from app.models.forms import LoginForm

@lm.user_loader
def load_user(session_token):
    return User.query.filter_by(id=session_token).first()

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash('Logged in')
            return redirect(url_for('index'))

        flash('Invalid login')

    return render_template('login.html',
                           form = form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Logged out')
    return redirect(url_for('login'))

@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')
