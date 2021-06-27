from ... import db


class QuizGameQuestionQuestionAnswer(db.Model):

    __tablename__ = 'quiz_game_question_question_answers'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    quizgamequestion_id = db.Column(
        db.Integer(),
        db.ForeignKey(
            'quiz_game_questions.id',
            ondelete='CASCADE'
        )
    )

    quizgamequestionanswer_id = db.Column(
        db.Integer(),
        db.ForeignKey(
            'quiz_game_question_answers.id',
            ondelete='CASCADE'
        )
    )
