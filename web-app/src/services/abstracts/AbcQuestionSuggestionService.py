from abc import ABC, abstractmethod
from typing import List

class AbcQuestionSuggestionService(ABC):

    @abstractmethod
    def add_answer_for_questionsuggestion(text, is_correct, quiz_suggestion_id) -> bool:
        raise NotImplementedError