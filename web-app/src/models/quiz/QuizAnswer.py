from ... import db


class QuizAnswer(db.Model):

    __tablename__ = 'quiz_answers'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    text = db.Column(
        db.String(),
        index=False,
        unique=False,
        nullable=False
    )

    is_correct = db.Column(
        db.Boolean()
    )

    quiz_question_id = db.Column(
        db.Integer,
        db.ForeignKey('quiz_questions.id'),
        nullable=False
    )
