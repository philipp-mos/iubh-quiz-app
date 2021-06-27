from flask_login import current_user
from datetime import datetime

from .abstracts.AbcQuizService import AbcQuizService

from ..models.quizgame.QuizGame import QuizGame
from ..models.quizgame.QuizGameStatus import QuizGameStatus


class QuizService(AbcQuizService):

    @staticmethod
    def initialize_quiz_game_for_subject(subject_id: int) -> QuizGame:
        quiz_game = QuizGame()
        quiz_game.creation_date = datetime.now()
        quiz_game.current_assignee_id = current_user.get_id()
        quiz_game.current_status = QuizGameStatus.IN_PROGRESS
        quiz_game.subject_id = subject_id

        return quiz_game
