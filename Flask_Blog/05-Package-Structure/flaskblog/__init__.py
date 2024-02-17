from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users/roberttimlin/Documents/GitHub/python-dev/Flask_Blog/06-Login-Auth/flaskblog/site.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root/Jedi2023@127.0.0.1/dev'
db = SQLAlchemy(app)

from flaskblog import routes
