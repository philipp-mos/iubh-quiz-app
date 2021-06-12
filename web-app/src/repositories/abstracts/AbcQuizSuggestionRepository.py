from abc import abstractmethod
from .AbcRepository import AbcRepository

class AbcQuizSuggestionRepository(AbcRepository):
    
    @abstractmethod
    def count_items_created_by_user_id(user_id):
        raise NotImplementedError

    
    @abstractmethod
    def count_approved_items_created_by_user_id(user_id):
        raise NotImplementedError