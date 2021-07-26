from abc import abstractmethod
from typing import List

from .AbcRepository import AbcRepository

from ...models.highscore.HighscoreRank import HighscoreRank


class AbcHighscoreRankRepository(AbcRepository):

    def get_all_ordered_by_rank(limit=0) -> List[HighscoreRank]:
        raise NotImplementedError

    @abstractmethod
    def find_by_rank(rank: int) -> HighscoreRank:
        raise NotImplementedError

    @abstractmethod
    def get_last_updated_item() -> HighscoreRank:
        raise NotImplementedError
