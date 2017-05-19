# -*- coding: utf-8 -*-

from app import app

@app.route('/hello')
@app.route('/')
def index():
    return 'Hello world!'

@app.route('/greeting', defaults={'name':None})
@app.route('/greeting/<name>')
def greeting(name):
    if name:
        return 'Olá, %s!' % name

    return 'Olá, usuário!'

@app.route('/user/<int:id>', methods=['GET'])
def user(id):
    return 'User id is %i!' % id