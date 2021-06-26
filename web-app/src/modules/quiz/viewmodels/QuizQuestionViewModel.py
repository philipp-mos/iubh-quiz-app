from typing import List
from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField, RadioField
from wtforms.validators import DataRequired


class QuizQuestionViewModel(FlaskForm):

    def __init__(self, question_text: str, answers: List[str]):
        self.question_text = question_text
        self.answers = answers

    question_number = HiddenField(
        'question-number',
        validators=[
            DataRequired()
        ]
    )

    selected_answer_flag = RadioField(choices=[('1', 'first'), ('2', 'second'), ('3', 'third')])

    submit = SubmitField('Diese Frage auswerten')
