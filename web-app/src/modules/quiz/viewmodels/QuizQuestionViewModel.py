from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField


class QuizQuestionViewModel(FlaskForm):

    question_text: str = ''

    answers = {}

    question_number: int = 0

    subject_name: str = ''

    # Form-Elements

    answer_selection = RadioField()

    submit = SubmitField()
