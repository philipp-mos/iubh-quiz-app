from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField
from wtforms.validators import DataRequired


class SubjectSelectionViewModel(FlaskForm):
    
    subject_id = HiddenField(
        'subject-id',
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField('Nächster Schritt')