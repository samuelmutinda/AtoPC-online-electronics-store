from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from sqlalchemy.sql import exists
# from datafiles.models import Manufacturer, Customer, Category

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI']   = 'sqlite:///appdatabase.db'
app.config['SECRET_KEY'] = 'eea013094d828aeb51a619aa'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)

from datafiles import routes