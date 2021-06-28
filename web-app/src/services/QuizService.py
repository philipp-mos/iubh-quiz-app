from flask import current_app as app
from flask_login import current_user
from datetime import datetime

from .abstracts.AbcQuizService import AbcQuizService

from ..models.quizgame.QuizGame import QuizGame
from ..models.quizgame.QuizGameQuestion import QuizGameQuestion
from ..models.quizgame.QuizGameQuestionAnswer import QuizGameQuestionAnswer
from ..models.quizgame.QuizGameStatus import QuizGameStatus

from ..repositories.QuizGameRepository import QuizGameRepository
from ..repositories.QuizQuestionRepository import QuizQuestionRepository
from ..repositories.QuizAnswerRepository import QuizAnswerRepository


class QuizService(AbcQuizService):

    @staticmethod
    def initialize_quiz_game_for_subject(subject_id: int) -> QuizGame:
        quiz_game = QuizGame()
        quiz_game.creation_date = datetime.now()
        quiz_game.current_assignee_id = current_user.get_id()
        quiz_game.current_status = QuizGameStatus.IN_PROGRESS
        quiz_game.subject_id = subject_id

        quiz_game_question = QuizService.get_random_question_and_answers_for_subject(subject_id)
        quiz_game.quizgamequestions.append(quiz_game_question)

        quiz_game_question_2 = QuizService.get_random_question_and_answers_for_subject(subject_id)
        quiz_game.quizgamequestions.append(quiz_game_question_2)

        QuizGameRepository.add_and_commit(quiz_game)

        return quiz_game

    @staticmethod
    def get_random_question_and_answers_for_subject(subject_id: int) -> QuizGameQuestion:

        quiz_question = QuizQuestionRepository.get_random_entry_by_subject_id(subject_id)

        if not quiz_question:
            return None

        quizgame_question = QuizGameQuestion()
        quizgame_question.quizquestion_id = quiz_question.id
        quizgame_question.quizquestion_text = quiz_question.question

        for count in range(app.config.get('AMOUNT_OF_ANSWERS_PER_QUESTION')):
            quiz_answer = QuizAnswerRepository.get_random_entry_by_question_id(quiz_question.id)

            if not quiz_answer:
                continue

            quizgame_question_answer = QuizGameQuestionAnswer()
            quizgame_question_answer.quizgame_question_id = quiz_question.id
            quizgame_question_answer.quizanswer_id = quiz_answer.id
            quizgame_question_answer.quizanswer_text = quiz_answer.text
            quizgame_question_answer.quizanswer_is_correct = quiz_answer.is_correct

            quizgame_question.quizgamequestionanswers.append(quizgame_question_answer)

        return quizgame_question
