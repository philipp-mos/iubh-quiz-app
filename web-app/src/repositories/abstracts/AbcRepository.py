from abc import ABC, abstractmethod


class AbcRepository(ABC):

    @abstractmethod
    def get_all():
        raise NotImplementedError

    @abstractmethod
    def find_by_id(id):
        raise NotImplementedError

    @abstractmethod
    def add_and_commit(item) -> None:
        raise NotImplementedError

    @abstractmethod
    def update_and_commit(item) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete_and_commit(item) -> None:
        raise NotImplementedError

    @abstractmethod
    def add(item) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(item) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(item) -> None:
        raise NotImplementedError

    @abstractmethod
    def commit() -> None:
        raise NotImplementedError
