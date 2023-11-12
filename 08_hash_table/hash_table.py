"""
Hash table.
"""

from functools import reduce
from operator import __add__

class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return reduce(__add__, (ord(ch) for ch in value), 0) % self.size

    def seek_slot(self, value):
        result = self.hash_fun(value)
        for _ in range(self.size):
            if self.slots[result] == value or self.slots[result] is None:
                return result
            result = (result + self.step) % self.size
        return None

    def put(self, value):
        if (index := self.seek_slot(value)) != None:
            self.slots[index] = value
            return index
        return None

    def find(self, value):
        result = self.hash_fun(value)
        for _ in range(self.size):
            if self.slots[result] == value:
                return result
            result = (result + self.step) % self.size
        return None
