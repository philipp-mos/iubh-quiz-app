from flask import current_app as app
from typing import List

from .abstracts.AbcQuizGameRepository import AbcQuizGameRepository
from .Repository import Repository
from ..models.quizgame.QuizGame import QuizGame
from ..models.quizgame.QuizGameStatus import QuizGameStatus


class QuizGameRepository(Repository, AbcQuizGameRepository):
    DEFAULT_RESULT_ITEM_MAX_COUNT = app.config['DEFAULT_RESULT_ITEM_MAX_COUNT']

    @staticmethod
    def get_all(limit=DEFAULT_RESULT_ITEM_MAX_COUNT) -> List[QuizGame]:
        """
        Returns all available Items
        """
        return QuizGame.query.all()[:limit]

    @staticmethod
    def find_by_id(id) -> QuizGame:
        """
        Get a specific Item by ID
        """
        return QuizGame.query.get(id)

    @staticmethod
    def get_all_by_status(quizgame_status: QuizGameStatus, current_user_id: int, limit=DEFAULT_RESULT_ITEM_MAX_COUNT) -> List[QuizGame]:
        return QuizGame.query.filter(
            QuizGame.current_status == quizgame_status,
            QuizGame.current_assignee_id != current_user_id)[:limit]
