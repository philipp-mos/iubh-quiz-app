from typing import List
from flask import current_app as app

from .abstracts.AbcQuizSuggestionService import AbcQuizSuggestionService

from ..repositories.QuizSuggestionRepository import QuizSuggestionRepository
from ..repositories.QuizSuggestionAnswerRepository import QuizSuggestionAnswerRepository
from ..repositories.SubjectRepository import SubjectRepository

from ..models.suggestquestion.QuizSuggestionAnswer import QuizSuggestionAnswer
from ..modules.user.viewmodels.UserProfileQuizSuggestionViewModel import UserProfileQuizSuggestionViewModel
from ..modules.tutor.viewmodels.TutorSuggestionViewModel import TutorSuggestionViewModel
from ..modules.tutor.viewmodels.TutorSuggestionAnswerViewModel import TutorSuggestionAnswerViewModel


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
            if quizsuggestion.is_approved is True:
                amount_approved = amount_approved + 1

        return UserProfileQuizSuggestionViewModel(
            len(quizsuggestions_by_user),
            amount_approved
        )

    @staticmethod
    def build_tutor_suggestion_overview_viewmodellist() -> List[TutorSuggestionViewModel]:
        """
        Builds and returns List of TUtorSuggestionViewModel with all active QuizSuggestions
        """
        viewmodel_list = []

        all_quizsuggestions = QuizSuggestionRepository.get_all_active()

        for quizsuggestion in all_quizsuggestions:
            viewmodel = TutorSuggestionViewModel()

            viewmodel.id = quizsuggestion.id
            viewmodel.date = quizsuggestion.creation_date.strftime('%d.%m.%Y %H:%M')
            viewmodel.question_text = quizsuggestion.question

            subject = SubjectRepository.find_by_id(quizsuggestion.subject_id)
            viewmodel.subject_name = subject.name

            viewmodel_list.append(viewmodel)

        return viewmodel_list

    @staticmethod
    def build_tutor_detail_viewmodel(suggestion_id: int) -> TutorSuggestionViewModel:
        """
        Builds the Detail Part of TutorSuggestionViewModel with Answers
        """
        viewmodel = TutorSuggestionViewModel()

        quizsuggestion = QuizSuggestionRepository.find_by_id(suggestion_id)

        viewmodel.id = quizsuggestion.id
        viewmodel.date = quizsuggestion.creation_date.strftime('%d.%m.%Y %H:%M')
        viewmodel.question_text = quizsuggestion.question

        subject = SubjectRepository.find_by_id(quizsuggestion.subject_id)
        viewmodel.subject_name = subject.name

        viewmodel.answer_viewmodels = []

        for quizsuggestionanswer in quizsuggestion.answers:
            answerviewmodel = TutorSuggestionAnswerViewModel()
            answerviewmodel.id = quizsuggestionanswer.id
            answerviewmodel.answer_text = quizsuggestionanswer.text
            answerviewmodel.is_correct = quizsuggestionanswer.is_correct

            viewmodel.answer_viewmodels.append(answerviewmodel)

        return viewmodel

    @staticmethod
    def is_invalid_suggestion_id(suggestion_id: int) -> bool:
        """
        Checks, if a QuizSuggestion is invalide
        """

        return not QuizSuggestionRepository.find_by_id(suggestion_id)
