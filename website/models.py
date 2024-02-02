# Database models (schema)

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.String(150))
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    notes = db.relationship('Note')   # Here, the comment below has been ignored, "FACEPALM for SQL"

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))   # This 'user' is the DB class User. 
                                                               #It is just SQL syntax to write it as lowercase for foreign keys.