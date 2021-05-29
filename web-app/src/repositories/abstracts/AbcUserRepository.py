from abc import abstractmethod

from .AbcRepository import AbcRepository

class AbcUserRepository(AbcRepository):

    @abstractmethod
    def find_by_email(user_email):
        raise NotImplementedError

    @abstractmethod
    def is_tutor_by_userid(user_id):
        raise NotImplementedError
