from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginViewModel(FlaskForm):

    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Bitte geben Sie eine gültige Email an')
        ]
    )

    password = PasswordField(
        'Passwort',
        validators=[DataRequired()]
    )

    submit = SubmitField('Anmelden')
