
class UserProfileViewModel():

    def __init__(self, email, is_email_verified, registered_since, role_status):
        
        self.email = email
        self.is_email_verified = is_email_verified
        self.registered_since = registered_since
        self.role_status = role_status