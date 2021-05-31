from wtforms import Form, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class SignupViewModel(Form):

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

    submit = SubmitField('Registrieren')
