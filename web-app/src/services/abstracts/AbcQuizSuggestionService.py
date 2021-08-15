from typing import List
from abc import ABC, abstractmethod

from ...modules.tutor.viewmodels.TutorSuggestionViewModel import TutorSuggestionViewModel
from ...modules.user.viewmodels.UserProfileQuizSuggestionViewModel import UserProfileQuizSuggestionViewModel


class AbcQuizSuggestionService(ABC):

    @abstractmethod
    def add_answer_for_quizsuggestion(text, is_correct, quiz_suggestion_id) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_stat_values_for_user_profile_by_user_id(user_id) -> UserProfileQuizSuggestionViewModel:
        raise NotImplementedError

    @abstractmethod
    def build_tutor_suggestion_overview_viewmodellist() -> List[TutorSuggestionViewModel]:
        raise NotImplementedError
