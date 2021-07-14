from ... import db


class QuizGameQuizGameQuestionScore(db.Model):

    __tablename__ = 'quiz_game_quiz_game_question_scores'

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

    quizgamequestionscore_id = db.Column(
        db.Integer(),
        db.ForeignKey(
            'quiz_game_question_scores.id',
            ondelete='CASCADE'
        )
    )
