from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class WebUser(db.Model):
    __tablename__='WebUser'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(64))
    userid = db.Column(db.String(32))
    username = db.Column(db.String(8))
