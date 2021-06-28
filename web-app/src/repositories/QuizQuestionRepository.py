from sqlalchemy.sql import func

from flask import current_app as app
from typing import List

from .abstracts.AbcQuizQuestionRepository import AbcQuizQuestionRepository
from .Repository import Repository
from ..models.quiz.QuizQuestion import QuizQuestion


class QuizQuestionRepository(Repository, AbcQuizQuestionRepository):
    DEFAULT_RESULT_ITEM_MAX_COUNT = app.config['DEFAULT_RESULT_ITEM_MAX_COUNT']

    @staticmethod
    def get_all(limit=DEFAULT_RESULT_ITEM_MAX_COUNT) -> List[QuizQuestion]:
        """
        Returns all available Items
        """
        return QuizQuestion.query.all()[:limit]

    @staticmethod
    def find_by_id(id) -> QuizQuestion:
        """
        Get a specific Item by ID
        """
        return QuizQuestion.query.get(id)

    @staticmethod
    def get_random_entry_by_subject_id(subject_id: int) -> QuizQuestion:
        """
        Pick a random Entry for given subject_id
        """
        return QuizQuestion.query.filter_by(subject_id=subject_id).order_by(func.random()).first()
