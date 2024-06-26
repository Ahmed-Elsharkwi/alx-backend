#!/usr/bin/env python3
"""
BasicCache class
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    class FIFOCache that inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """ put some items in the dictionary """
        if key is not None and item is not None:
            length = len(self.cache_data)
            if length == BaseCaching.MAX_ITEMS:
                count = 0
                for key_1 in self.cache_data:
                    if key != key_1:
                        if count == (length - 1):
                            print(f"DISCARD: {key_1}")
                            del self.cache_data[key_1]
                            break
                    else:
                        break
                    count += 1
            self.cache_data[key] = item

    def get(self, key):
        """ return the value in the dicionary """
        if key is None or key not in self.cache_data:
            return None
        else:
            value = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = value
            return value
