from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField, StringField
from wtforms.validators import DataRequired


class SubjectSelectionViewModel(FlaskForm):
    
    subject_id = HiddenField(
        'subject-id',
        validators=[
            DataRequired()
        ]
    )

    subject_name = StringField(
        'subject-name',
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField('Nächster Schritt')