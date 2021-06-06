from ... import db

class QuizSuggestion(db.Model):

    __tablename__ = 'quiz_suggestions'


    id = db.Column(
        db.Integer,
        primary_key=True
    )

    question = db.Column(
        db.String(),
        index=False,
        unique=True,
        nullable=False
    )

    creation_date = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )

    is_approved = db.Column(
        db.Boolean()
    )

    is_declined = db.Column(
        db.Boolean()
    )



    answers = db.relationship(
        'QuizSuggestionAnswer',
        backref='quiz_suggestions',
        lazy=True
    )
    

    subject_id = db.Column(
        db.Integer,
        db.ForeignKey('subjects.id'),
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )
