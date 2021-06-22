from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Regexp


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
            Regexp(
                regex='^(?:(?=.*[a-z])(?:(?=.*[A-Z])(?=.*[\d\W])|(?=.*\W)(?=.*\d))|(?=.*\W)(?=.*[A-Z])(?=.*\d)).{12,}$',
                message='Bitte wähle ein stärkeres Passwort. Dein Passwort muss mindestens 12 Zeichen, davon mindestens 1 Sonderzeichen und eine Zahl, enthalten.'
            )
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
