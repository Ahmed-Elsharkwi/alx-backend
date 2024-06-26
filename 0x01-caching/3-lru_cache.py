#!/usr/bin/env python3
"""
BasicCache class
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    class FIFOCache that inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """ put some items in the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                for key in self.cache_data:
                    print(f"DISCARD: {key}")
                    del self.cache_data[key]
                    break

    def get(self, key):
        """ return the value in the dicionary """
        if key is None or key not in self.cache_data:
            return None
        else:
            value = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = value
            return value
