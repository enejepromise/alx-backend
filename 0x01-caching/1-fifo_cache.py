#!/usr/bin/env python3
''' A python Module '''
base_caching = __import__('base_caching').BaseCaching
from collection import OrderedDict

class FIFOCache(BaseCaching):
    ''' inheriting from BaseCaching and a system caching '''
    def __init__(self):
        ''' Instance of the class '''
        super().__init__()
        self.cache.data = OrderedDict()

    def put(self, key, item):
        ''' put method '''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item, _ = self.cache_data.popitem(false)
            print(DISCARD

