import sqlalchemy.exc
from app import db


class Users (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(20))
    passport_number = db.Column(db.String(10), default=None)
    international_passport_number = db.Column(db.String(9), default=None)
    phone_number = db.Column(db.String(12))
    mail = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(15))
    surname = db.Column(db.String(15))
    patronymic = db.Column(db.String(20))
    rights = db.Column(db.Integer, default=0)
    # 0 это обычный юзер, 1 это менеджер, 2 это администратор, 3 это admin


    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)


class Tours (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    price = db.Column(db.Integer)
    photo = db.Column(db.String(200))
    description = db.Column(db.String(1000))
    Direction = db.Column(db.String(50))

    def __init__(self, *args, **kwargs):
        super(Tours, self).__init__(*args, **kwargs)


class Booking (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_tours = db.Column(db.Integer)
    id_user = db.Column(db.Integer)
    datetime = db.Column(db.DateTime)

    def __init__(self, *args, **kwargs):
        super(Booking, self).__init__(*args, **kwargs)







