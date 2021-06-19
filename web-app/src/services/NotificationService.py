from .abstracts.AbcNotificationService import AbcNotificationService


class NotificationService(AbcNotificationService):

    @staticmethod
    def send_notification(receiver_email, subject, html_content):
        raise NotImplementedError
