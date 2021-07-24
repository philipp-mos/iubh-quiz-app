from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField
from wtforms.validators import DataRequired, Length

from .UserProfileQuizSuggestionViewModel import UserProfileQuizSuggestionViewModel


class UserProfileViewModel(FlaskForm):

    email: str = ''

    is_email_verified: bool = False

    registered_since: str = ''

    role_status: str = ''

    # Highscore
    is_highscore_enabled = BooleanField('Zeige mich in der Highscore-Übersicht')

    highscore_alias = StringField(
        'Alias',
        validators=[
            DataRequired(),
            Length(min=5)
        ]
    )

    user_profile_quiz_suggestion: UserProfileQuizSuggestionViewModel

    submit = SubmitField('Speichern')
