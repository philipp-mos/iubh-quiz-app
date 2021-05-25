from abc import abstractmethod

from .AbcRepository import AbcRepository

class AbcUserRepository(AbcRepository):

    @abstractmethod
    def find_by_email(user_email):
        return NotImplementedError
