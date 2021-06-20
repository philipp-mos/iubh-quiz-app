import time

from flask import current_app as app


class CacheManager(object):

    _cache_ = {}
    EXPIRES = 1
    VALUE = 0

    @classmethod
    def get_from_key(self, key: str):
        """
        Returns Value from Cache by Key
        Deletes Key if Cached Value is expired
        """
        try:
            if self._cache_[key][self.EXPIRES] > time.time():
                return self._cache_[key][self.VALUE]
            else:
                del self._cache_[key]
                return None
        except KeyError:
            return None

    @classmethod
    def set_by_key(self, key: str, value, duration=3600):
        """
        Add Value to Cache by CachingKey
        """
        try:
            expire_time = time.time() + duration
        except TypeError:
            app.logger.error('')
            raise TypeError("Dureation should be a numeric value")

        self._cache_[key] = (value, expire_time)

        return self.get_from_key(key)

    # Cache Keys
    _APPVERSION = '_AppVersion'
