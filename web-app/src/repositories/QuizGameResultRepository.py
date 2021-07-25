from flask import current_app as app
from typing import List

from .abstracts.AbcQuizGameResultRepository import AbcQuizGameResultRepository
from .Repository import Repository
from ..models.quizgame.QuizGameResult import QuizGameResult


class QuizGameResultRepository(Repository, AbcQuizGameResultRepository):
    DEFAULT_RESULT_ITEM_MAX_COUNT = app.config['DEFAULT_RESULT_ITEM_MAX_COUNT']

    @staticmethod
    def get_all(limit=DEFAULT_RESULT_ITEM_MAX_COUNT) -> List[QuizGameResult]:
        """
        Returns all available Items
        """
        return QuizGameResult.query.all()[:limit]

    @staticmethod
    def find_by_id(id) -> QuizGameResult:
        """
        Get a specific Item by ID
        """
        return QuizGameResult.query.get(id)

    @staticmethod
    def count_by_user_id(user_id: int) -> int:
        return QuizGameResult.query.filter(QuizGameResult.user_id == user_id).count()
