from .. import login_manager

from .abstracts.AbcUserService import AbcUserService

class UserService(AbcUserService):

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)