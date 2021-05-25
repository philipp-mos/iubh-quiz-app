from .. import login_manager

class UserService:

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)