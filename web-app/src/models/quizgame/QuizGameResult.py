from ... import db


class QuizGameResult(db.Model):

    __tablename__ = 'quiz_game_results'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    is_won = db.Column(
        db.Boolean()
    )

    creation_date = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )

    quizgame_id = db.Column(
        db.Integer,
        db.ForeignKey('quiz_games.id'),
        nullable=False
    )
