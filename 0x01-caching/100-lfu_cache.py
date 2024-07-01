#!/usr/bin/env python3
"""
BasicCache class
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    class FIFOCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ assign something """
        self.counter = {}
        super().__init__()

    def put(self, key, item):
        """ put some items in the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                item_1 = ''
                keys_list = list(self.cache_data.keys())
                counter = self.counter[keys_list[-2]]
                i = len(keys_list) - 2

                while i >= 0:
                    if counter >= self.counter[keys_list[i]]:
                        counter = self.counter[keys_list[i]]
                        item_1 = keys_list[i]
                    i -= 1

                print(f"DISCARD: {item_1}")
                del self.cache_data[item_1]
                del self.counter[item_1]

            self.counter[key] = 1

    def get(self, key):
        """ return the value in the dicionary """
        if key is None or key not in self.cache_data:
            return None
        else:
            value = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = value
            self.counter[key] = self.counter[key] + 1
            return value
