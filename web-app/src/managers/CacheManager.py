import time


class CacheManager(object):

    _cache_ = {}
    EXPIRES = 0
    VALUE = 1

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
