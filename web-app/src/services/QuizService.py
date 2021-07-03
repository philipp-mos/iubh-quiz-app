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

from ..modules.quiz.viewmodels.QuizQuestionViewModel import QuizQuestionViewModel

from ..repositories.SubjectRepository import SubjectRepository
from ..repositories.QuizGameRepository import QuizGameRepository
from ..repositories.QuizQuestionRepository import QuizQuestionRepository
from ..repositories.QuizAnswerRepository import QuizAnswerRepository


class QuizService(AbcQuizService):

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

        viewmodel.answers = {}

        quizgame_answer: QuizGameQuestionAnswer
        for quizgame_answer in quiz_game_question.quizgamequestionanswers:
            viewmodel.answers[chr(ord('@') + quizgame_answer.position)] = quizgame_answer.quizanswer_text

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
                    chr(ord('@') + number),
                    chr(ord('`') + number)
                )
            )
