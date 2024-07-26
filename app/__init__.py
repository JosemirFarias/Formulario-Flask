from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'AA65S4D65D46A4D98AS4D98A98S4D9A8S4D98A4S9D849A8'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.views import home
from app.models import User