from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class SignupViewModel(FlaskForm):

    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Bitte geben Sie eine gültige Email an')
        ]
    )

    password = PasswordField(
        'Passwort',        
        validators=[
            DataRequired(),
            Length(min=8, message='Bitte wähle ein längeres Passwort.')
        ]
    )

    password_confirm = PasswordField(
        'Passwort wiederholen',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwörter müssen übereinstimmen.')
        ]
    )

    privacypolicy_accepted = BooleanField(
        'Ich akzeptiere die Datenschutzerklärung',
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField('Registrieren')
