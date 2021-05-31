from abc import ABC, abstractmethod


class AbcNotificationService(ABC):

    @abstractmethod
    def send_notification(receiver_email, subject, html_content):
        raise NotImplementedError
