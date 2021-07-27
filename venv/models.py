from __init__ import db
#from venv import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())  #automatically adds date and stores in a date/time obj
    # setting up a relationship between notes and users. One user - many notes.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #stores a key in a child object that references a parent class below (user = User, .id = id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) #uniqe key to each user (e.g. if names are the same)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')  #stores


