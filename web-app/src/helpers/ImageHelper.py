import urllib
import hashlib
from typing import List

from flask import current_app as app


class ImageHelper:

    @staticmethod
    def build_gavatar_image_url(user_email: str) -> str:
        """
        Builds a Gravatar Image Url
        """
        image_size: int = 45

        gravatar_url: List[str] = []

        gravatar_url.append(app.config.get('GRAVATAR_URL'))
        gravatar_url.append(
            hashlib.md5(
                user_email.lower().encode(
                    app.config.get('APP_ENCODING_TYPE')
                )
            ).hexdigest()
        )
        gravatar_url.append('?')
        gravatar_url.append(
            urllib.parse.urlencode(
                {
                    'd': 'retro',
                    's': str(image_size)
                }
            )
        )

        return ''.join(gravatar_url)
