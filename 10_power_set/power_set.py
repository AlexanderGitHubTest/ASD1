"""
Power set.
"""

from functools import reduce
from operator import __add__

class PowerSet():

    # INIT_SIZE = 20011  # The initial size of the array is the first prime number after 20000
    # INIT_SIZE = 40011  # The initial size of the array is the first prime number after 40000
    INIT_SIZE = 99991 # The initial size of the array is the maximum prime number less than 100000
    STEP = 3 # Step size for the sequential sampling method (a variant of the linear collision resolution method)

    def __init__(self):
        self.HT = HashTable(self.INIT_SIZE, self.STEP)

    def __resize(self):
        new_HT = HashTable(self.HT.size * 2, self.STEP)
        for elem in self.HT.slots:
            if not elem is None:
                new_HT.put(elem)
        self.HT = new_HT

    def size(self):
        return reduce(__add__, ((lambda elem: 0 if elem is None else 1)(elem) for elem in self.HT.slots), 0)

    def put(self, value):
        index = self.HT.put(value)
        if index is None:
            self.__resize()
            self.HT.put(value)           

    def get(self, value):
        if not self.HT.find(value) is None:
            return True
        return False    

    def remove(self, value):
        if not (index := self.HT.find(value)) is None:
            self.HT.slots[index] = None
            return True
        return False    

    def intersection(self, set2):
        result = PowerSet()
        empty_set = True
        for elem in self.HT.slots:
            if not elem is None and set2.get(elem):
                empty_set = False
                result.put(elem)
        if not empty_set:
            return result
        return None

    def union(self, set2):
        result = PowerSet()
        empty_set = True
        for elem in self.HT.slots:
            if not elem is None:
                empty_set = False
                result.put(elem)
        for elem in set2.HT.slots:
            if not elem is None:
                empty_set = False
                result.put(elem)
        if not empty_set:
            return result
        return None

    def difference(self, set2):
        result = PowerSet()
        empty_set = True
        for elem in self.HT.slots:
            if not elem is None and not set2.get(elem):
                empty_set = False
                result.put(elem)
        if not empty_set:
            return result
        return None

    def issubset(self, set2):
        for elem in set2.HT.slots:
            if not elem is None and not self.get(elem):
                return False
        return True


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
            if self.slots[result] is None:
                return None
            result = (result + self.step) % self.size
        return None
