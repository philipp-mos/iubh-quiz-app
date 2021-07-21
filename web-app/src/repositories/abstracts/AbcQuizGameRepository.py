from abc import abstractmethod
from typing import List
from .AbcRepository import AbcRepository

from ...models.quizgame.QuizGame import QuizGame
from ...models.quizgame.QuizGameStatus import QuizGameStatus


class AbcQuizGameRepository(AbcRepository):

    @abstractmethod
    def get_all_by_status(quizgame_status: QuizGameStatus, limit=0) -> List[QuizGame]:
        raise NotImplementedError
