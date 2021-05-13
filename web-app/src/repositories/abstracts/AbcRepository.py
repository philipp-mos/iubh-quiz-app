from abc import ABC, abstractmethod

class AbcRepository(ABC):

    @abstractmethod
    def get_all():
        raise NotImplementedError

    @abstractmethod
    def get_by_id(id):
        raise NotImplementedError