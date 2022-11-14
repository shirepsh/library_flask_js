import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

"""
in this file we are responsible for create the app, database setup, register blueprints
"""

#create app
app = Flask(__name__)
CORS(app)
app.config["TEMPLATES_AUTO_RELOAD"] = True 
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_library.sqlite3'

app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"http://127.0.0.1:5000": {"origins": "*"}})

##########################################
############ DATABASE SETUP ##############
##########################################

#create a db and connect to the sqlitAlchemy
 
db = SQLAlchemy(app)

##########################################
######### REGISTER BLUEPRINTS ############
##########################################

from project.books.views import books
from project.core.views import core
from project.customers.views import customers
from project.loans.views import loans

app.register_blueprint(books)
app.register_blueprint(core)
app.register_blueprint(customers)
app.register_blueprint(loans)


with app.app_context():
    db.create_all()