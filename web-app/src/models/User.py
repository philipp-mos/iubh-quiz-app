from .. import db
from flask_login import UserMixin

class User(UserMixin, db.Model):

    __tablename__ = 'users'


    id = db.Column(
        db.Integer,
        primary_key=True
    )

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(200),
        primary_key=False,
        unique=False,
        nullable=False
	)

    creation_date = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )

