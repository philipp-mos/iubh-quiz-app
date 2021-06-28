from abc import ABC, abstractmethod

from ...models.quizgame.QuizGame import QuizGame
from ...models.quizgame.QuizGameQuestion import QuizGameQuestion


class AbcQuizService(ABC):

    @abstractmethod
    def initialize_quiz_game_for_subject(subject_id: int) -> QuizGame:
        raise NotImplementedError

    @abstractmethod
    def get_random_question_and_answers_for_subject(subject_id: int, position: int) -> QuizGameQuestion:
        raise NotImplementedError
