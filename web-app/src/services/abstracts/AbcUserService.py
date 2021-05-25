from abc import ABC, abstractmethod

class AbcUserService(ABC):

    @abstractmethod
    def load_user(user_id):
        raise NotImplementedError