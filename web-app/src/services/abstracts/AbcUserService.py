from abc import ABC, abstractmethod

from ...models.User import User

class AbcUserService(ABC):

    @abstractmethod
    def load_user(user_id):
        raise NotImplementedError

    @abstractmethod
    def unauthorized():
        raise NotImplementedError

    @abstractmethod
    def check_password(User, password):
        raise NotImplementedError
