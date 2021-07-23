from flask_wtf import FlaskForm
from wtforms import BooleanField

from .UserProfileQuizSuggestionViewModel import UserProfileQuizSuggestionViewModel


class UserProfileViewModel(FlaskForm):

    email: str = ''

    is_email_verified: bool = False

    is_highscore_enabled = BooleanField('Zeige mich in der Highscore-Übersicht')

    registered_since: str = ''

    role_status: str = ''

    user_profile_quiz_suggestion: UserProfileQuizSuggestionViewModel
