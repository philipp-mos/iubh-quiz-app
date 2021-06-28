from flask import current_app as app
from typing import List

from .abstracts.AbcQuizAnswerRepository import AbcQuizAnswerRepository
from .Repository import Repository
from ..models.quiz.QuizAnswer import QuizAnswer


class QuizAnswerRepository(Repository, AbcQuizAnswerRepository):
    DEFAULT_RESULT_ITEM_MAX_COUNT = app.config['DEFAULT_RESULT_ITEM_MAX_COUNT']

    @staticmethod
    def get_all(limit=DEFAULT_RESULT_ITEM_MAX_COUNT) -> List[QuizAnswer]:
        """
        Returns all available Items
        """
        return QuizAnswer.query.all()[:limit]

    @staticmethod
    def find_by_id(id) -> QuizAnswer:
        """
        Get a specific Item by ID
        """
        return QuizAnswer.query.get(id)
