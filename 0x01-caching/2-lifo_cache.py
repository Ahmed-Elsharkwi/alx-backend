#!/usr/bin/env python3
"""
BasicCache class
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    class FIFOCache that inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """ put some items in the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item
            length = len(self.cache_data)
            if length  > BaseCaching.MAX_ITEMS:
                count = 0
                for key_1 in self.cache_data:
                    if count == (length - 2):
                        print(f"DISCARD: {key_1}")
                        del self.cache_data[key_1]
                        break
                    count += 1

    def get(self, key):
        """ return the value in the dicionary """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
