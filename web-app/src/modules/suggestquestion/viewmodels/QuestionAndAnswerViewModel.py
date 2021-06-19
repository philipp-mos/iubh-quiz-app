from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length


class QuestionAndAnswerViewModel(FlaskForm):

    subject_id = HiddenField(
        'subject-id',
        validators=[
            DataRequired()
        ]
    )

    question_text = StringField(
        'Wie lautet deine Quiz-Frage?',
        validators=[
            DataRequired(),
            Length(min=10, message="Deine Frage sollte mindestens 10 Zeichen enthalten.")
        ]
    )

    answer_1_text = StringField(
        'Bitte nenne uns eine Antwortmöglichkeit',
        validators=[
            DataRequired(),
        ]
    )

    answer_2_text = StringField(
        'Bitte nenne uns eine Antwortmöglichkeit',
        validators=[
            DataRequired(),
        ]
    )

    answer_3_text = StringField(
        'Bitte nenne uns eine Antwortmöglichkeit',
        validators=[
            DataRequired()
        ]
    )

    correct_answer_flag = RadioField(choices=[('1', 'first'), ('2', 'second'), ('3', 'third')])

    submit = SubmitField('Anfrage absenden')
