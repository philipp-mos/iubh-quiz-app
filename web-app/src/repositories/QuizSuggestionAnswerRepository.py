from flask import current_app as app
from typing import List

from .abstracts.AbcQuizSuggestionAnswerRepository import AbcQuizSuggestionAnswerRepository
from .Repository import Repository

from ..models.suggestquestion.QuizSuggestionAnswer import QuizSuggestionAnswer


class QuizSuggestionAnswerRepository(Repository, AbcQuizSuggestionAnswerRepository):
    DEFAULT_RESULT_ITEM_MAX_COUNT = app.config['DEFAULT_RESULT_ITEM_MAX_COUNT']

    @staticmethod
    def get_all(limit=DEFAULT_RESULT_ITEM_MAX_COUNT) -> List[QuizSuggestionAnswer]:
        """
        Returns all available Items
        """
        return QuizSuggestionAnswer.query.all()[:limit]

    @staticmethod
    def find_by_id(id) -> QuizSuggestionAnswer:
        """
        Get a specific Item by ID
        """
        return QuizSuggestionAnswer.query.get(id)
