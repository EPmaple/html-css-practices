from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#referring to the local python file, flask instance is requiring to receive
#this parameter
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

from market import routes #python trying to execute what's inside that file
from market import models