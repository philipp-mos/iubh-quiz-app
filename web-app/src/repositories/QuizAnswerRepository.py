from sqlalchemy.sql import func

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

    @staticmethod
    def get_random_entry_by_question_id(question_id: int, is_correct: bool = False) -> QuizAnswer:
        """
        Pick a random Entry for given question_id
        """
        return QuizAnswer.query.filter_by(quiz_question_id=question_id, is_correct=is_correct).order_by(func.random()).first()
