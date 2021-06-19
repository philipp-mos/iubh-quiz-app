from abc import abstractmethod

from ...models.user import UserRole
from .AbcRepository import AbcRepository


class AbcUserRoleRepository(AbcRepository):

    @abstractmethod
    def find_by_name(name) -> UserRole:
        raise NotImplementedError
