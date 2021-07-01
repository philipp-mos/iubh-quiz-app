from abc import abstractmethod
from .AbcRepository import AbcRepository

from ...models.quiz.QuizAnswer import QuizAnswer


class AbcQuizAnswerRepository(AbcRepository):

    @abstractmethod
    def get_random_entry_by_question_id(question_id: int, is_correct: bool = False) -> QuizAnswer:
        raise NotImplementedError
