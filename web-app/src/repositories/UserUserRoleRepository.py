from .abstracts.AbcUserUserRoleRepository import AbcUserUserRoleRepository
from .Repository import Repository
from ..models.user import UserUserRole


class UserUserRoleRepository(Repository, AbcUserUserRoleRepository):

    @staticmethod
    def get_all():
        """
        Returns all available Items
        """
        return UserUserRole.query.all()

    @staticmethod
    def find_by_id(id) -> UserUserRole:
        """
        Get a specific Item by ID
        """
        return UserUserRole.query.get(id)
