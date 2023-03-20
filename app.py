from flask import flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://orders.db'
db = SQLAlchemy(app)


class Orders(db.Model):
    id = db.Column(db.string(36), primary_key =  True)
    status = db.Column(db.string(20), nullable=False)
    items = db.Column(db.JSON, nullable=False)
    total = db.Column(db.Float, nullable=False)
    currency_unit = db.Column(db.String(10), nullable=False)