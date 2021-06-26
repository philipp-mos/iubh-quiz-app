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

    quizgame_setup_id = db.Column(
        db.Integer,
        db.ForeignKey('quiz_game_setups.id'),
        nullable=False
    )
