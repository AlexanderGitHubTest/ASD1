"""
Native cache.
"""

from functools import reduce
from operator import __add__

class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        return reduce(__add__, (ord(ch) for ch in key), 0) % self.size

    def seek_slot(self, key):
        result = self.hash_fun(key)
        min_hits = {"index": result, "value": self.hits[result]}
        for _ in range(self.size):
            if self.slots[result] == key or self.slots[result] is None:
                return result
            result = (result + 1) % self.size
            if self.hits[result] < min_hits["value"]:
                min_hits = {"index": result, "value": self.hits[result]}
        self.slots[min_hits["index"]] = None
        self.values[min_hits["index"]] = None
        self.hits[min_hits["index"]] = 0
        return min_hits["index"]

    def is_key(self, key):
        result = self.hash_fun(key)
        for _ in range(self.size):
            if self.slots[result] == key:
                return True
            result = (result + 1) % self.size
        return False

    def put(self, key, value):
        index = self.seek_slot(key)
        self.slots[index] = key
        self.values[index] = value       

    def get(self, key):
        result = self.hash_fun(key)
        for _ in range(self.size):
            if self.slots[result] == key:
                self.hits[result] += 1
                return self.values[result]
            result = (result + 1) % self.size
        return None
