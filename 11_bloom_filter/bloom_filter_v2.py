"""
Bloom filter (the filter is not filled with test data during initialization).
"""

class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 0

    def hash1(self, str1):
        random_number = 17
        result = 0
        for c in str1:
            code = ord(c)
            result = (result * random_number + code) % 2 ** self.filter_len
        return result

    def hash2(self, str1):
        random_number = 223
        result = 0
        for c in str1:
            code = ord(c)
            result = (result * random_number + code) % 2 ** self.filter_len
        return result

    def add(self, str1):
        self.filter = self.filter | self.hash1(str1)
        self.filter = self.filter | self.hash2(str1)

    def is_value(self, str1):
        str1_hash = self.hash1(str1) | self.hash2(str1)
        return self.filter & str1_hash == str1_hash
