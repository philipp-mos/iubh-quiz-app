from .. import db


class Tutor(db.Model):

    __tablename__ = 'tutors'


    id = db.Column(
        db.Integer,
        primary_key=True
    )

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    subject_id = db.Column(
        db.Integer,
        db.ForeignKey('subject.id'),
        nullable=False)
