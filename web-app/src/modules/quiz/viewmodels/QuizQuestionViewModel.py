from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, BooleanField


class QuizQuestionViewModel(FlaskForm):

    question_text: str = ''

    answers = []

    question_number: int = 0

    subject_name: str = ''

    answer_selection = RadioField()

    is_validation_step = BooleanField()

    submit = SubmitField()
