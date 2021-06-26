from ... import db


class QuizGameSetup(db.Model):

    __tablename__ = 'quiz_game_setups'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    quizquestion_text = db.Column(
        db.String(),
        index=False,
        unique=False,
        nullable=False
    )

    quizquestion_id = db.Column(
        db.Integer,
        db.ForeignKey('quiz_questions.id'),
        nullable=False
    )
