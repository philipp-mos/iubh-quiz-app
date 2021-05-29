from abc import abstractmethod

from .AbcRepository import AbcRepository

class AbcUserRoleRepository(AbcRepository):

    @abstractmethod
    def find_by_name(name):
        raise NotImplementedError
