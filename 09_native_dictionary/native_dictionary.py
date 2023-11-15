"""
Native_dictionary.
"""

from functools import reduce
from operator import __add__

class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        return reduce(__add__, (ord(ch) for ch in key), 0) % self.size

    def seek_slot(self, key):
        result = self.hash_fun(key)
        for _ in range(self.size):
            if self.slots[result] == key or self.slots[result] is None:
                return result
            result = (result + 1) % self.size
        raise Exception("Overflow of an associative array!")

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
                return self.values[result]
            result = (result + 1) % self.size
        return None
