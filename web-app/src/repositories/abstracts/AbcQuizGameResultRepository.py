from abc import abstractmethod
from typing import List
from .AbcRepository import AbcRepository

from ...models.quizgame.QuizGameResult import QuizGameResult


class AbcQuizGameResultRepository(AbcRepository):

    @abstractmethod
    def find_by_guizgame_id(quizgame_id: int, limit=0) -> List[QuizGameResult]:
        raise NotImplementedError

    @abstractmethod
    def get_all_grouped_and_count_by_user() -> List[QuizGameResult]:
        raise NotImplementedError

    @abstractmethod
    def get_quizgameresults_by_userid_ytd(user_id: int) -> List[QuizGameResult]:
        raise NotImplementedError
