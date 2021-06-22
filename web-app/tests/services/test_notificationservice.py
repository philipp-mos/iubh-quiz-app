import pytest

from src.services.NotificationService import NotificationService


def test_notificationservice_send_notification():
    with pytest.raises(NotImplementedError) as exception:
        NotificationService.send_notification('email@test.com', 'Email-Subject', 'Sample Content')
