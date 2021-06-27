from ... import db


class QuizGameQuestionAnswer(db.Model):

    __tablename__ = 'quiz_game_question_answers'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    quizanswer_text = db.Column(
        db.String(),
        index=False,
        unique=False,
        nullable=False
    )

    quizanswer_is_correct = db.Column(
        db.Boolean()
    )

    quizanswer_id = db.Column(
        db.Integer,
        db.ForeignKey('quiz_answers.id'),
        nullable=False
    )

    quizgame_question_id = db.Column(
        db.Integer,
        db.ForeignKey('quiz_game_questions.id'),
        nullable=False
    )
