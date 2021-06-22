import time

from flask import current_app as app


class CacheManager(object):

    _cache_ = {}
    EXPIRES = 1
    VALUE = 0

    # Caching Time Constants
    _ONEDAY = 86400
    _HALFDAY = 43200
    _ONEHOUR = 3600
    _TENMINUTE = 600
    _ONEMINUTE = 60

    @classmethod
    def get_from_key(self, key: str):
        """
        Returns Value from Cache by Key
        Deletes Key if Cached Value is expired
        """

        if app.config.get('IS_CACHING_ENABLED'):
            return None

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
            error_message = 'Cache-Duration should be a numeric value'
            app.logger.error(error_message)
            raise TypeError(error_message)

        self._cache_[key] = (value, expire_time)

        return value

    @classmethod
    def purge_cache(self):
        """
        Empties the Cache
        """
        self._cache_ = {}
        app.logger.info('App Cache has been successfully purged.')

    # Cache Keys
    _APPVERSION = '_AppVersion'
    _BUNDLEVERSION = '_BundleVersion'
    _GETALLSUBJECTSAPIDTO = '_GetAllSubjectsApiDto'
    _GETALLSUBJECTSORDEREDBYNAME = '_GetAllSubjectsOrderedByName'
