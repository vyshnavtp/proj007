import os
import os.path as op
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin




UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}






app = Flask(__name__)
app.config['SECRET_KEY'] = '718a4ee2b889319dca57cf8b929cac22'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['FLASK_ADMIN_SWATCH'] = 'Cyborg'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)





file_path = op.join(op.dirname(__file__),'static/turfphotos')
try :
  os.mkdir(file_path)
except OSError:
   pass



bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from carp import routes
from carp import admins

