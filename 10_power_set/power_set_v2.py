"""
Power set v2. (Converted to a standard list (was based on HashTable))
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
        empty_set = True
        set2_set = set(set2.list)
        for elem in self.list:
            if elem in set2_set:
                empty_set = False
                result.put(elem)
        if not empty_set:
            return result
        return None

    def union(self, set2):
        result = PowerSet()
        empty_set = True
        for elem in self.list:
            empty_set = False
            result.put(elem)
        for elem in set2.list:
            empty_set = False
            result.put(elem)
        if not empty_set:
            return result
        return None

    def difference(self, set2):
        result = PowerSet()
        empty_set = True
        set2_set = set(set2.list)
        for elem in self.list:
            if not (elem in set2_set):
                empty_set = False
                result.put(elem)
        if not empty_set:
            return result
        return None

    def issubset(self, set2):
        self_set = set(self.list)
        for elem in set2.list:
            if not (elem in self_set):
                return False
        return True
