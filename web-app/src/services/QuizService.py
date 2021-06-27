from .abstracts.AbcQuizService import AbcQuizService

from ..models.quizgame.QuizGame import QuizGame


class QuizService(AbcQuizService):

    @staticmethod
    def initialize_quiz_game_for_subject(subject_id: int) -> QuizGame:
        pass
