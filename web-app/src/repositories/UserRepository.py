from .abstracts.AbcUserRepository import AbcUserRepository
from .Repository import Repository
from ..models.user.User import User


class UserRepository(Repository, AbcUserRepository):
    
    def get_all():
        return User.query.all()

    def find_by_id(id):
        return User.query.get(id)

    def find_by_email(user_email):
        return User.query.filter_by(email=user_email).first()