import random
from flask import current_app as app
from flask_login import current_user
from datetime import datetime

from .abstracts.AbcQuizService import AbcQuizService

from ..models.subject.Subject import Subject
from ..models.quiz.QuizQuestion import QuizQuestion
from ..models.quiz.QuizAnswer import QuizAnswer
from ..models.quizgame.QuizGame import QuizGame
from ..models.quizgame.QuizGameQuestion import QuizGameQuestion
from ..models.quizgame.QuizGameQuestionAnswer import QuizGameQuestionAnswer
from ..models.quizgame.QuizGameStatus import QuizGameStatus
from ..models.quizgame.QuizGameQuestionScore import QuizGameQuestionScore
from ..models.quizgame.QuizGameResult import QuizGameResult

from ..modules.quiz.viewmodels.QuizQuestionViewModel import QuizQuestionViewModel
from ..modules.quiz.viewmodels.QuizQuestionAnswerViewModel import QuizQuestionAnswerViewModel

from ..repositories.SubjectRepository import SubjectRepository
from ..repositories.QuizGameRepository import QuizGameRepository
from ..repositories.QuizQuestionRepository import QuizQuestionRepository
from ..repositories.QuizAnswerRepository import QuizAnswerRepository
from ..repositories.QuizGameResultRepository import QuizGameResultRepository

from ..helpers.NumberHelper import NumberHelper


class QuizService(AbcQuizService):

    # region Public Static Methods
    @staticmethod
    def initialize_quiz_game_for_subject(subject_id: int) -> QuizGame:
        """
        Build initial QuizGame and fill with random Questions and Answers from Subject
        """

        quiz_game = QuizGame()
        quiz_game.creation_date = datetime.now()
        quiz_game.current_assignee_id = current_user.get_id()
        quiz_game.current_status = QuizGameStatus.IN_PROGRESS
        quiz_game.subject_id = subject_id

        for count in range(app.config.get('AMOUNT_OF_QUESTIONS_PER_QUIZ')):
            quiz_game_question: QuizGameQuestion = QuizService.get_random_question_and_answers_for_subject(subject_id, count + 1)

            if not quiz_game_question:
                # TODO: Implement proper Error Handling
                raise Exception

            quiz_game.quizgamequestions.append(quiz_game_question)

        QuizGameRepository.add_and_commit(quiz_game)

        return quiz_game

    @staticmethod
    def get_random_question_and_answers_for_subject(subject_id: int, position: int) -> QuizGameQuestion:
        """
        Load a random Question and random Answers based on Subject
        """

        quiz_question: QuizQuestion = QuizQuestionRepository.get_random_entry_by_subject_id(subject_id)

        if not quiz_question:
            return None

        quizgame_question = QuizGameQuestion()
        quizgame_question.quizquestion_id = quiz_question.id
        quizgame_question.quizquestion_text = quiz_question.question
        quizgame_question.position = position

        correct_answer = random.randint(0, (int(app.config.get('AMOUNT_OF_ANSWERS_PER_QUESTION')) - 1))

        for count in range(app.config.get('AMOUNT_OF_ANSWERS_PER_QUESTION')):

            quiz_answer: QuizAnswer = QuizAnswerRepository.get_random_entry_by_question_id(
                quiz_question.id,
                count == correct_answer
            )

            if not quiz_answer:
                return None

            quizgame_question_answer = QuizGameQuestionAnswer()
            quizgame_question_answer.quizanswer_id = quiz_answer.id
            quizgame_question_answer.quizanswer_text = quiz_answer.text
            quizgame_question_answer.quizanswer_is_correct = quiz_answer.is_correct
            quizgame_question_answer.position = count + 1

            quizgame_question.quizgamequestionanswers.append(quizgame_question_answer)

        return quizgame_question

    @staticmethod
    def fill_quizquestionviewmodel_by_quizgame_id(viewmodel: QuizQuestionViewModel, quizgame_id: int, question_number: int) -> None:
        """
        Build the QuizQuestionViewModel by QuizGame Id and current Question-Number
        """
        quiz_game: QuizGame = QuizGameRepository.find_by_id(quizgame_id)

        if not quiz_game:
            raise ValueError

        subject: Subject = SubjectRepository.find_by_id(quiz_game.subject_id)

        if not subject:
            raise ValueError

        viewmodel.subject_name = subject.name

        quiz_game_question: QuizGameQuestion = quiz_game.quizgamequestions[question_number - 1]

        viewmodel.question_text = quiz_game_question.quizquestion_text

        viewmodel.question_number = question_number

        if app.config.get('SHOW_QUESTIONRESULTS_ONLY_SUMMARIZED') or viewmodel.is_validation_step.data:
            viewmodel.submit.label.text = 'Weiter'
        else:
            viewmodel.submit.label.text = 'Diese Frage auswerten'

        viewmodel.answers = []

        quizgame_answer: QuizGameQuestionAnswer
        for quizgame_answer in quiz_game_question.quizgamequestionanswers:
            quiz_questionanswer_viewmodel = QuizQuestionAnswerViewModel()

            quiz_questionanswer_viewmodel.answer_char = NumberHelper.convert_from_number_to_char(quizgame_answer.position, True)
            quiz_questionanswer_viewmodel.answer_text = quizgame_answer.quizanswer_text

            quiz_questionanswer_viewmodel.mark_correct = False
            quiz_questionanswer_viewmodel.mark_incorrect = False

            if viewmodel.answer_selection.data == quiz_questionanswer_viewmodel.answer_char:
                if quizgame_answer.quizanswer_is_correct:
                    quiz_questionanswer_viewmodel.mark_correct = True
                else:
                    quiz_questionanswer_viewmodel.mark_incorrect = True

            viewmodel.answers.append(quiz_questionanswer_viewmodel)

        QuizService.add_answer_selection_choices(viewmodel)

    @staticmethod
    def add_answer_selection_choices(quizquestion_viewmodel: QuizQuestionViewModel) -> None:
        """
        Dynamically add the Coices for RadioButton Formelement
        """
        quizquestion_viewmodel.answer_selection.choices = []

        for count in range(app.config.get('AMOUNT_OF_ANSWERS_PER_QUESTION')):
            number = count + 1

            quizquestion_viewmodel.answer_selection.choices.append(
                (
                    NumberHelper.convert_from_number_to_char(number, True),
                    NumberHelper.convert_from_number_to_char(number)
                )
            )

    @staticmethod
    def update_quiz_game_status_to(quiz_id: int, quiz_game_status: QuizGameStatus) -> None:
        """
        Updates the status of the current QuizGame
        """
        if not quiz_id:
            raise ValueError

        quiz_game = QuizGameRepository.find_by_id(int(quiz_id))

        quiz_game.current_status = quiz_game_status

        QuizGameRepository.commit()

    @staticmethod
    def save_quiz_game_question_score(quiz_game_id: int, question_number: int, viewmodel: QuizQuestionViewModel) -> None:
        """
        Builds the QuizGame QuestionScore Model and persists it
        """
        quiz_game: QuizGame = QuizGameRepository.find_by_id(quiz_game_id)

        quiz_game_question: QuizGameQuestion = QuizService.__get_quiz_game_question(
            quiz_game.quizgamequestions,
            question_number
        )

        quiz_game_question_score = QuizGameQuestionScore()
        quiz_game_question_score.creation_date = datetime.now()
        quiz_game_question_score.quizgame_id = quiz_game.id
        quiz_game_question_score.assigned_user_id = current_user.get_id()
        quiz_game_question_score.quizgamequestion_id = quiz_game_question.id

        quiz_game_question_score.selected_quizgamequestionanswer_id = QuizService.__get_answer_id_for_selected_answer(
            quiz_game_question.quizgamequestionanswers,
            NumberHelper.convert_from_char_to_number(viewmodel.answer_selection.data)
        )

        quiz_game_question_score.correct_quizgamequestionanswer_id = QuizService.__get_answer_id_for_correct_answer(
            quiz_game_question.quizgamequestionanswers
        )

        quiz_game_question_score.is_solved_correctly = (
            quiz_game_question_score.correct_quizgamequestionanswer_id == quiz_game_question_score.selected_quizgamequestionanswer_id
        )

        quiz_game.quizgamequestionscores.append(quiz_game_question_score)

        QuizGameRepository.commit()

    @staticmethod
    def save_and_get_quiz_game_result(quizgame_id: int) -> QuizGameResult:
        quizgame_result = QuizGameResult()
        quizgame_result.quizgame_id = quizgame_id
        quizgame_result.user_id = int(current_user.get_id())
        quizgame_result.creation_date = datetime.now()

        # TODO: Update as soon as opponent-mode is implemented
        quizgame_result.is_won = False

        quizgame_result.amount_of_questions = 0
        quizgame_result.amount_of_correct_questions = 0

        quiz_game: QuizGame = QuizGameRepository.find_by_id(quizgame_id)

        for questionscore in quiz_game.quizgamequestionscores:
            if questionscore.assigned_user_id == int(current_user.get_id()):
                quizgame_result.amount_of_questions += 1

                if questionscore.is_solved_correctly:
                    quizgame_result.amount_of_correct_questions += 1

        QuizGameResultRepository.add_and_commit(quizgame_result)

        return quizgame_result
    # endregion

    # region Private Methods
    @staticmethod
    def __get_quiz_game_question(quizgame_questions, question_number: int) -> QuizGameQuestion:
        """
        Returns the Selected Answer Id
        """
        quiz_game_question: QuizGameQuestion

        for quizgame_question in quizgame_questions:
            if quizgame_question.position == question_number:
                quiz_game_question = quizgame_question
                break

        if not quiz_game_question:
            app.logger.error('QuizGameQuestion could not be defined')
            raise ValueError

        return quiz_game_question

    @staticmethod
    def __get_answer_id_for_selected_answer(quizgame_question_answers, selected_number: int) -> int:
        """
        Returns the Selected Answer Id
        """
        selected_answer_id: int

        for quizgame_question_answer in quizgame_question_answers:
            if quizgame_question_answer.position == selected_number:
                selected_answer_id = quizgame_question_answer.id
                break

        if not selected_answer_id:
            app.logger.error('Selected Answer Id could not be defined')
            raise ValueError

        return selected_answer_id

    @staticmethod
    def __get_answer_id_for_correct_answer(quizgame_question_answers) -> int:
        """
        Returns the Correct Answer Id
        """
        correct_answer_id: int

        for quizgame_question_answer in quizgame_question_answers:
            if quizgame_question_answer.quizanswer_is_correct:
                correct_answer_id = quizgame_question_answer.id
                break

        if not correct_answer_id:
            app.logger.error('Correct Answer Id could not be defined')
            raise ValueError

        return correct_answer_id
    # endregion
