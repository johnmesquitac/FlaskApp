from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY']= SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #criamos uma espécie de servidor local em SQL para armazenar os usuários do blog
db = SQLAlchemy(app) #criação de um data base em SQL
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from app import routes