from abc import ABC, abstractmethod

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

    @abstractmethod
    def set_password(User, password):
        raise NotImplementedError

    @abstractmethod
    def verify_recaptcha(captcha_response, user_remote_ip):
        raise NotImplementedError


    @abstractmethod
    def is_user_student(user: User) -> bool:
        raise NotImplementedError

    @abstractmethod
    def is_user_tutor(user: User) -> bool:
        raise NotImplementedError