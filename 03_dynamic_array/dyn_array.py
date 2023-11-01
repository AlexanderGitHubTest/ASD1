"""
Dynamic array.
"""

import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        if i == self.count:
            self.array[self.count] = itm
        else:        
            for pos in range(self.count, i, -1):
                self.array[pos] = self.array[pos-1]
            self.array[i] = itm
        self.count += 1

    def delete(self, i):
        # Minimum buffer fill percentage
        MINIMUM_BUFFER_FILL_PERCENTAGE = 50
        # How much do I need to reduce the buffer
        HOW_MUCH_REDUCE_BUFFER = 1.5
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        for pos in range(i, self.count - 1):
            self.array[pos] = self.array[pos+1]
        self.count -= 1
        if self.capacity > 16 and self.count < int(self.capacity * MINIMUM_BUFFER_FILL_PERCENTAGE / 100):
            self.resize(16 if (new_size:= int(self.capacity / HOW_MUCH_REDUCE_BUFFER)) <= 16 else new_size)
