from wtforms import Form, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginViewModel(Form):

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
