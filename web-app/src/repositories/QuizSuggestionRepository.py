from flask import current_app as app
from typing import List

from .abstracts.AbcQuizSuggestionRepository import AbcQuizSuggestionRepository
from .Repository import Repository

from ..models.suggestquestion.QuizSuggestion import QuizSuggestion


class QuizSuggestionRepository(Repository, AbcQuizSuggestionRepository):
    DEFAULT_RESULT_ITEM_MAX_COUNT = app.config['DEFAULT_RESULT_ITEM_MAX_COUNT']

    @staticmethod
    def get_all(limit = DEFAULT_RESULT_ITEM_MAX_COUNT) -> List[QuizSuggestion]:
        """
        Returns all available Items
        """
        return QuizSuggestion.query.all()[:limit]


    @staticmethod
    def find_by_id(id) -> QuizSuggestion:
        """
        Get a specific Item by ID
        """
        return QuizSuggestion.query.get(id)


    @staticmethod
    def count_items_created_by_user_id(user_id):
        """
        Returns the amount of elements created by specific user_id
        """
        return len(QuizSuggestion.query.filter_by(user_id=user_id).all())


    @staticmethod
    def count_approved_items_created_by_user_id(user_id):
        """
        Returns the amount of approved elements created by specific user_id
        """
        return len(QuizSuggestion.query.filter_by(user_id=user_id, is_approved=True).all())
