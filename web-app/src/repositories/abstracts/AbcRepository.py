from abc import ABC, abstractmethod

class AbcRepository(ABC):

    @abstractmethod
    def get_all():
        raise NotImplementedError

    @abstractmethod
    def find_by_id(id):
        raise NotImplementedError

    @abstractmethod
    def add(item):
        raise NotImplementedError

    @abstractmethod
    def update(item):
        raise NotImplementedError

    @abstractmethod
    def delete(item):
        raise NotImplementedError
