from abc import ABC, abstractmethod

from ...modules.user.viewmodels.UserProfileQuizSuggestionViewModel import UserProfileQuizSuggestionViewModel

class AbcQuizSuggestionService(ABC):

    @abstractmethod
    def add_answer_for_quizsuggestion(text, is_correct, quiz_suggestion_id) -> bool:
        raise NotImplementedError


    @abstractmethod
    def get_stat_values_for_user_profile_by_user_id(user_id) -> UserProfileQuizSuggestionViewModel:
        raise NotImplementedError