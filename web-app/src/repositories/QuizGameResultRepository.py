from sqlalchemy.sql import func
from flask import current_app as app
from typing import List
from datetime import datetime

from .. import db

from .abstracts.AbcQuizGameResultRepository import AbcQuizGameResultRepository
from .Repository import Repository
from ..models.quizgame.QuizGameResult import QuizGameResult


class QuizGameResultRepository(Repository, AbcQuizGameResultRepository):
    DEFAULT_RESULT_ITEM_MAX_COUNT = app.config['DEFAULT_RESULT_ITEM_MAX_COUNT']

    @staticmethod
    def get_all(limit=DEFAULT_RESULT_ITEM_MAX_COUNT) -> List[QuizGameResult]:
        """
        Returns all available Items
        """
        return QuizGameResult.query.all()[:limit]

    @staticmethod
    def find_by_id(id) -> QuizGameResult:
        """
        Get a specific Item by ID
        """
        return QuizGameResult.query.get(id)

    @staticmethod
    def find_by_guizgame_id(quizgame_id: int, limit=DEFAULT_RESULT_ITEM_MAX_COUNT) -> List[QuizGameResult]:
        """
        Returns all QuizGameResults for a given QuizGame Id
        """
        return QuizGameResult.query.filter(QuizGameResult.quizgame_id == quizgame_id)[:limit]

    @staticmethod
    def count_by_user_id(user_id: int) -> int:
        return QuizGameResult.query.filter(QuizGameResult.user_id == user_id).count()

    @staticmethod
    def get_all_grouped_and_count_by_user() -> List[QuizGameResult]:
        """
        Return Values Grouped and Count by User_Id
        """
        return db.session.query(
            QuizGameResult.user_id,
            func.count('*').label('amount_of_games_won')
        ).filter(
            QuizGameResult.is_won == True  # noqa: E712
        ).group_by(
            QuizGameResult.user_id
        )

    @staticmethod
    def get_quizgameresults_by_userid(user_id: int) -> List[QuizGameResult]:
        """
        Returns all Items by UserId in current year
        """
        return QuizGameResult.query.filter(
            QuizGameResult.user_id == user_id,
            QuizGameResult.creation_date >= datetime(datetime.today().year, 1, 1),
            QuizGameResult.creation_date <= datetime(datetime.today().year, 12, 31),
        )
