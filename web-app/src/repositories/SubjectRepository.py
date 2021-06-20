from flask import current_app as app
from typing import List

from .abstracts.AbcSubjectRepository import AbcSubjectRepository
from .Repository import Repository
from ..models.Subject import Subject


class SubjectRepository(Repository, AbcSubjectRepository):
    DEFAULT_RESULT_ITEM_MAX_COUNT = app.config['DEFAULT_RESULT_ITEM_MAX_COUNT']

    @staticmethod
    def get_all(limit=DEFAULT_RESULT_ITEM_MAX_COUNT) -> List[Subject]:
        """
        Returns all available Items
        """
        return Subject.query.all()[:limit]

    @staticmethod
    def find_by_id(id) -> Subject:
        """
        Get a specific Item by ID
        """
        return Subject.query.get(id)

    @staticmethod
    def search_by_query(query, limit=DEFAULT_RESULT_ITEM_MAX_COUNT) -> List[Subject]:
        """
        Search Subjects based on given Query-String
        """
        return Subject.query.filter(Subject.name.contains(query))[:limit]
