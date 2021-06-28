from abc import abstractmethod
from .AbcRepository import AbcRepository

from ...models.quiz.QuizQuestion import QuizQuestion


class AbcQuizQuestionRepository(AbcRepository):

    @abstractmethod
    def get_random_entry_by_subject_id(subject_id: int) -> QuizQuestion:
        raise NotImplementedError
