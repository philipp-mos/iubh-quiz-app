from .abstracts.AbcUserRoleRepository import AbcUserRoleRepository
from .Repository import Repository
from ..models.user.UserRole import UserRole


class UserRoleRepository(Repository, AbcUserRoleRepository):

    @staticmethod
    def get_all():
        """
        Returns all available Items
        """
        return UserRole.query.all()


    @staticmethod
    def find_by_id(id):
        """
        Get a specific Item by ID
        """
        return UserRole.query.get(id)


    @staticmethod
    def find_by_name(name):
        """
        Get a specific Item by Name
        """
        return UserRole.query.filter_by(name=name).first()
