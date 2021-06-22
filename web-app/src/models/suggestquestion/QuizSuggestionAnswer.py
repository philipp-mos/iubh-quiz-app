from ... import db


class QuizSuggestionAnswer(db.Model):

    __tablename__ = 'quiz_suggestion_answers'

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

    quiz_suggestion_id = db.Column(
        db.Integer,
        db.ForeignKey('quiz_suggestions.id'),
        nullable=False
    )
