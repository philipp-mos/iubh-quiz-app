from flask import current_app as app
from typing import List

from .abstracts.AbcHighscoreRankRepository import AbcHighscoreRankRepository
from .Repository import Repository
from ..models.highscore.HighscoreRank import HighscoreRank


class HighscoreRankRepository(Repository, AbcHighscoreRankRepository):
    DEFAULT_RESULT_ITEM_MAX_COUNT = app.config['DEFAULT_RESULT_ITEM_MAX_COUNT']

    @staticmethod
    def get_all(limit=DEFAULT_RESULT_ITEM_MAX_COUNT) -> List[HighscoreRank]:
        """
        Returns all available Items
        """
        return HighscoreRank.query.all()[:limit]

    @staticmethod
    def find_by_id(id) -> HighscoreRank:
        """
        Get a specific Item by ID
        """
        return HighscoreRank.query.get(id)

    @staticmethod
    def find_by_rank(rank: int) -> HighscoreRank:
        """
        Get a specific HighscoreRank by rank
        """
        return HighscoreRank.query.filter(HighscoreRank.rank == rank).first()
