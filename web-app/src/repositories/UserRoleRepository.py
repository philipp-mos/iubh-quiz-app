from .abstracts.AbcUserRoleRepository import AbcUserRoleRepository
from .Repository import Repository
from ..models.user.UserRole import UserRole


class UserRoleRepository(Repository, AbcUserRoleRepository):

    def get_all():
        return UserRole.query.all()

    def find_by_id(id):
        return UserRole.query.get(id)

    def find_by_name(name):
        return UserRole.query.filter_by(name=name).first()
