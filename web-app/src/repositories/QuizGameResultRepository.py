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
    def find_by_guizgame_id(quizgame_id: int, limit=DEFAULT_RESULT_ITEM_MAX_COUNT) -> List[QuizGameResult]:
        """
        Returns all QuizGameResults for a given QuizGame Id
        """
        return QuizGameResult.query.filter(QuizGameResult.quizgame_id == quizgame_id)[:limit]
