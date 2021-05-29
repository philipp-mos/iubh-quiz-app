from abc import abstractmethod
from ...models.user import User

from .AbcRepository import AbcRepository

class AbcUserRepository(AbcRepository):

    @abstractmethod
    def find_by_email(user_email) -> User:
        raise NotImplementedError

    @abstractmethod
    def is_tutor_by_userid(user_id) -> User:
        raise NotImplementedError
