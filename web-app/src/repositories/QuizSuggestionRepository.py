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
