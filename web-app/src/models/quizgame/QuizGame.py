from sqlalchemy.dialects.postgresql import ENUM
from ... import db

from .QuizGameStatus import QuizGameStatus


class QuizGame(db.Model):

    __tablename__ = 'quiz_games'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    current_status = db.Column(
        ENUM(QuizGameStatus),
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

    subject_id = db.Column(
        db.Integer,
        db.ForeignKey('subjects.id'),
        nullable=False
    )

    quizgamequestions = db.relationship(
        'QuizGameQuestion',
        secondary='quiz_game_quiz_game_questions'
    )
