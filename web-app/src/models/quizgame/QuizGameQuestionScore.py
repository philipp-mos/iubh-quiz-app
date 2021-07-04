from ... import db


class QuizGameQuestionScore(db.Model):

    __tablename__ = 'quiz_game_question_scores'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    creation_date = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )

    quizgame_id = db.Column(
        db.Integer,
        db.ForeignKey('quiz_games.id'),
        nullable=False
    )

    quizgamequestion_id = db.Column(
        db.Integer,
        db.ForeignKey('quiz_game_questions.id'),
        nullable=False
    )

    correct_quizgamequestionanswer_id = db.Column(
        db.Integer,
        db.ForeignKey('quiz_game_question_answers.id'),
        nullable=False
    )

    selected_quizgamequestionanswer_id = db.Column(
        db.Integer,
        db.ForeignKey('quiz_game_question_answers.id'),
        nullable=False
    )

    is_solved_correctly = db.Column(
        db.Boolean()
    )
