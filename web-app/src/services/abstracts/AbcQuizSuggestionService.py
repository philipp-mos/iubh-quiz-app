from abc import ABC, abstractmethod
from typing import List

class AbcQuizSuggestionService(ABC):

    @abstractmethod
    def add_answer_for_quizsuggestion(text, is_correct, quiz_suggestion_id) -> bool:
        raise NotImplementedError