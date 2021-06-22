from flask import current_app as app
from typing import List

from .abstracts.AbcUserRepository import AbcUserRepository
from .Repository import Repository
from ..models.user.User import User


class UserRepository(Repository, AbcUserRepository):

    @staticmethod
    def get_all() -> List[User]:
        """
        Returns all available Items
        """
        return User.query.all()

    @staticmethod
    def find_by_id(id) -> User:
        """
        Get a specific Item by ID
        """
        return User.query.get(id)

    @staticmethod
    def find_by_email(user_email) -> User:
        """
        Get a specific User by Email
        """
        return User.query.filter_by(email=user_email).first()

    @staticmethod
    def find_active_by_email(user_email) -> User:
        """
        Get a active User by Email
        """
        return User.query.filter_by(is_active=True, email=user_email).first()

    @staticmethod
    def is_tutor_by_userid(user_id) -> bool:
        """
        Checks, if a Tutor-Role is assigned to a specific user
        """
        return len(User.query.filter_by(id=user_id).filter(User.roles.any(id=app.config['USERROLE_TUTOR'])).all()) > 0
