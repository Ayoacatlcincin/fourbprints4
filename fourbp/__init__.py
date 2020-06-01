import os
from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_DEFAULT_SENDER'] = "wareliteracing@gmail.com"
app.config['MAIL_USERNAME'] = "wareliteracing@gmail.com"
app.config['MAIL_PASSWORD'] = "Zapata99!"
mail = Mail(app)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = "mysecretkey"
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['TESTING'] = False
app.config['LOGIN_DISABLED'] = False
app.config['UPLOAD_FOLDER'] = basedir + '/upload'