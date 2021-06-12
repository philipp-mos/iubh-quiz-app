from flask import current_app as app
from typing import List

from .abstracts.AbcQuizSuggestionService import AbcQuizSuggestionService

from ..repositories.QuizSuggestionRepository import QuizSuggestionRepository
from ..repositories.QuizSuggestionAnswerRepository import QuizSuggestionAnswerRepository

from ..models.suggestquestion.QuizSuggestionAnswer import QuizSuggestionAnswer
from ..modules.user.viewmodels.UserProfileQuizSuggestionViewModel import UserProfileQuizSuggestionViewModel


class QuizSuggestionService(AbcQuizSuggestionService):

    @staticmethod
    def add_answer_for_quizsuggestion(text, is_correct, quiz_suggestion_id) -> bool:
        """
        Adds Answer related to QuizSuggestion to Database
        """
        new_answer = QuizSuggestionAnswer()
        new_answer.text = text
        new_answer.is_correct = is_correct
        new_answer.quiz_suggestion_id = quiz_suggestion_id

        QuizSuggestionAnswerRepository.add_and_commit(new_answer)

        if new_answer.id:
            return True
        else:
            app.logger.critical('New Answer for Quizsuggestion has not been created')
            return False



    @staticmethod
    def get_stat_values_for_user_profile_by_user_id(user_id) -> UserProfileQuizSuggestionViewModel:
        quizsuggestions_by_user = QuizSuggestionRepository.get_items_created_by_user_id(user_id)

        amount_approved = 0

        for quizsuggestion in quizsuggestions_by_user:
            if quizsuggestion.is_approved == True:
                amount_approved = amount_approved + 1


        return UserProfileQuizSuggestionViewModel(
            len(quizsuggestions_by_user),
            amount_approved
        )
