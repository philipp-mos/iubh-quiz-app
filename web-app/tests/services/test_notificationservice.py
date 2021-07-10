import pytest

from src.services.abstracts.AbcNotificationService import AbcNotificationService
from src.services.NotificationService import NotificationService


__notificationservice: AbcNotificationService = NotificationService()


def test_notificationservice_send_notification():
    with pytest.raises(NotImplementedError) as exception:  # noqa: F841
        __notificationservice.send_notification('email@test.com', 'Email-Subject', 'Sample Content')
