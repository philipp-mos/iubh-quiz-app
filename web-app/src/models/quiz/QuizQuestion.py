from ... import db


class QuizQuestion(db.Model):

    __tablename__ = 'quiz_questions'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    question = db.Column(
        db.String(),
        index=False,
        unique=False,
        nullable=False
    )

    subject_id = db.Column(
        db.Integer,
        db.ForeignKey('subjects.id'),
        nullable=False
    )

    tutor_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )
