from ... import db


class QuizGameQuizGameQuestion(db.Model):

    __tablename__ = 'quiz_game_quiz_game_questions'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    quizgame_id = db.Column(
        db.Integer(),
        db.ForeignKey(
            'quiz_games.id',
            ondelete='CASCADE'
        )
    )

    quizgamequestion_id = db.Column(
        db.Integer(),
        db.ForeignKey(
            'quiz_game_questions.id',
            ondelete='CASCADE'
        )
    )
