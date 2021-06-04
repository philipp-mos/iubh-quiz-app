from abc import abstractmethod
from typing import List

from ...models.Subject import Subject

from .AbcRepository import AbcRepository

class AbcSubjectRepository(AbcRepository):

    @abstractmethod
    def search_by_query(query) -> List[Subject]:
        raise NotImplementedError