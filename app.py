#!/usr/bin/env python3

""" 
Pruebas de deploy a flask app as https://docs.digitalocean.com/tutorials/app-deploy-flask-app/

"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Sammy!'

