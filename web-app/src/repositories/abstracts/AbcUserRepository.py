from abc import abstractmethod

from ...models.user.User import User
from .AbcRepository import AbcRepository


class AbcUserRepository(AbcRepository):

    @abstractmethod
    def find_by_email(user_email) -> User:
        raise NotImplementedError

    @abstractmethod
    def find_active_by_email(user_email) -> User:
        raise NotImplementedError

    @abstractmethod
    def find_by_useralias(user_alias: str) -> User:
        raise NotImplementedError

    @abstractmethod
    def is_tutor_by_userid(user_id) -> bool:
        raise NotImplementedError
