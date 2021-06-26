from ... import db


class QuizGame(db.Model):

    __tablename__ = 'quiz_games'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    status = db.Column(
        db.Integer,
        unique=False,
        nullable=False
    )

    creation_date = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )

    current_assignee_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )
