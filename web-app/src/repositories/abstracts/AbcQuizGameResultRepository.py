from abc import abstractmethod
from .AbcRepository import AbcRepository


class AbcQuizGameResultRepository(AbcRepository):

    @abstractmethod
    def count_by_user_id(user_id: int) -> int:
        raise NotImplementedError
