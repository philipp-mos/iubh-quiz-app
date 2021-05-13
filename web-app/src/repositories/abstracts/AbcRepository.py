from abc import ABC, abstractmethod

class AbcRepository(ABC):

    @abstractmethod
    def get_all():
        raise NotImplementedError

    @abstractmethod
    def find_by_id(id):
        raise NotImplementedError

    # def add()
    # def update()
    # def remove()
