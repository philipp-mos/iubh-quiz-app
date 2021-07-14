from ... import db


class QuizGameQuestion(db.Model):

    __tablename__ = 'quiz_game_questions'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    position = db.Column(
        db.Integer,
        unique=False,
        nullable=False
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

    quizgamequestionanswers = db.relationship(
        'QuizGameQuestionAnswer',
        secondary='quiz_game_question_question_answers'
    )
