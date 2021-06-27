from abc import ABC, abstractmethod

from ...models.quizgame.QuizGame import QuizGame


class AbcQuizService(ABC):

    @abstractmethod
    def initialize_quiz_game_for_subject(subject_id: int) -> QuizGame:
        raise NotImplementedError
