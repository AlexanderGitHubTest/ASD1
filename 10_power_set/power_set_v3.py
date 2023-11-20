"""
Power set v3. 
1. Converted to a standard list (was based on HashTable).
2. All operations on sets return the PowerSet type.
"""

class PowerSet():

    def __init__(self):
        self.list = []

    def size(self):
        return len(set(self.list))

    def put(self, value):
        self.list.append(value)

    def get(self, value):
        return (value in self.list)

    def remove(self, value):
        something_found = False
        need_remove = True       
        search_from = 0
        while need_remove:
            try:
                index_of_found = self.list.index(value, search_from)
            except ValueError:
                need_remove = False
            else:
                something_found = True
                del self.list[index_of_found]
                search_from = index_of_found
        return something_found

    def intersection(self, set2):
        result = PowerSet()
        set2_set = set(set2.list)
        for elem in self.list:
            if elem in set2_set:
                result.put(elem)
        return result

    def union(self, set2):
        result = PowerSet()
        for elem in self.list:
            result.put(elem)
        for elem in set2.list:
            empty_set = False
            result.put(elem)
        return result

    def difference(self, set2):
        result = PowerSet()
        set2_set = set(set2.list)
        for elem in self.list:
            if not (elem in set2_set):
                result.put(elem)
        return result

    def issubset(self, set2):
        self_set = set(self.list)
        for elem in set2.list:
            if not (elem in self_set):
                return False
        return True
