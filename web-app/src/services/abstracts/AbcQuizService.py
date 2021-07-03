from abc import ABC, abstractmethod

from ...models.quizgame.QuizGame import QuizGame
from ...models.quizgame.QuizGameQuestion import QuizGameQuestion
from ...models.quizgame.QuizGameStatus import QuizGameStatus

from ...modules.quiz.viewmodels.QuizQuestionViewModel import QuizQuestionViewModel


class AbcQuizService(ABC):

    @abstractmethod
    def initialize_quiz_game_for_subject(subject_id: int) -> QuizGame:
        raise NotImplementedError

    @abstractmethod
    def get_random_question_and_answers_for_subject(subject_id: int, position: int) -> QuizGameQuestion:
        raise NotImplementedError

    @abstractmethod
    def fill_quizquestionviewmodel_by_quizgame_id(viewmodel: QuizQuestionViewModel, quizgame_id: int, question_number: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_answer_selection_choices(quizquestion_viewmodel: QuizQuestionViewModel) -> None:
        raise NotImplementedError

    @abstractmethod
    def update_quiz_game_status_to(quiz_game_status: QuizGameStatus) -> None:
        raise NotImplementedError
