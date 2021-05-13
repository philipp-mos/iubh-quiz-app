from .. import db

class Subject(db.Model):

    __tablename__ = 'subjects'


    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(255),
        index=False,
        unique=True,
        nullable=False
    )
