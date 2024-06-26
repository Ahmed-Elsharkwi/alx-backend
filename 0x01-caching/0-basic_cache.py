#!/usr/bin/python3
"""
module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    class BasicCache that inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """ put some items in the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ return the value in the dicionary """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
