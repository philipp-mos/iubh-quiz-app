from .abstracts.AbcUserRepository import AbcUserRepository
from .. import db
from .Repository import Repository
from ..models.user.User import User


class UserRepository(Repository, AbcUserRepository):

    @staticmethod
    def get_all():
        """
        Returns all available Items
        """
        return User.query.all()


    @staticmethod
    def find_by_id(id):
        """
        Get a specific Item by ID
        """
        return User.query.get(id)


    @staticmethod
    def find_by_email(user_email):
        """
        Get a specific Item by Email
        """
        return User.query.filter_by(email=user_email).first()


    @staticmethod
    def is_tutor_by_userid(user_id):
        raise NotImplementedError
