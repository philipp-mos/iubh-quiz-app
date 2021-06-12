from abc import ABC, abstractmethod

class AbcQuizSuggestionService(ABC):

    @abstractmethod
    def add_answer_for_quizsuggestion(text, is_correct, quiz_suggestion_id) -> bool:
        raise NotImplementedError