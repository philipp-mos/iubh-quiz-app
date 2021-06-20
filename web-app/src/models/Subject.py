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

    short = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    image_path = db.Column(
        db.String(255),
        nullable=False
    )

    tutor_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False)

    def __init__(self, name) -> None:
        self.name = name
