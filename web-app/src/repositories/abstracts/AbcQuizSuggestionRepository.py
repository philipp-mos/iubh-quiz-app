from abc import abstractmethod
from typing import List
from .AbcRepository import AbcRepository

from ...models.suggestquestion.QuizSuggestion import QuizSuggestion


class AbcQuizSuggestionRepository(AbcRepository):

    @abstractmethod
    def get_items_created_by_user_id(user_id) -> List[QuizSuggestion]:
        raise NotImplementedError

    @abstractmethod
    def get_all_active(limit=0) -> List[QuizSuggestion]:
        raise NotImplementedError
