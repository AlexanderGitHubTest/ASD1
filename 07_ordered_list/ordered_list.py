"""
Ordered list.
"""

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2: 
            return -1
        if v1 == v2: 
            return 0
        if v1 > v2: 
            return 1

    def add(self, value):
        newNode = Node(value)
        
        if self.head == None and self.tail == None:
            newNode.next = None
            newNode.prev = None
            self.head = newNode
            self.tail = newNode
            return

        node = (self.head if self.__ascending else self.tail)
        before_node = None
        while node != None:
            if self.compare(value, node.value) < 1:
                before_node = node
                break
            node = (node.next if self.__ascending else node.prev)

        if self.__ascending and before_node is None:
            newNode.next = None
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            return
        if not self.__ascending and before_node is None:
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            return

        if self.__ascending and before_node.prev is None:
            newNode.next = before_node
            newNode.prev = None
            self.head.prev = newNode
            self.head = newNode
            return
        if not self.__ascending and before_node.next is None:
            newNode.prev = before_node
            newNode.next = None
            self.tail.next = newNode
            self.tail = newNode
            return
        if self.__ascending:
            newNode.next = before_node
            newNode.prev = before_node.prev
            before_node.prev.next = newNode        
            before_node.prev = newNode
            return
        newNode.prev = before_node
        newNode.next = before_node.next
        before_node.next.prev = newNode
        before_node.next = newNode

    def find(self, val):
        node = (self.head if self.__ascending else self.tail)
        while node != None:
            if self.compare(val, node.value) == -1:
                return None
            if self.compare(val, node.value) == 0:
                return node
            node = (node.next if self.__ascending else node.prev)
        return None

    def delete(self, val):
        if self.head == None and self.tail == None:
            return None
        node = (self.head if self.__ascending else self.tail)
        while node != None:
            if self.compare(val, node.value) == -1:
                return None
            if self.compare(val, node.value) == 0:
                break
            node = (node.next if self.__ascending else node.prev)

        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
            del node
            return

        if node is self.head:
            node.next.prev = None
            self.head = node.next
            del node
            return

        if node is self.tail:
            node.prev.next = None
            self.tail = node.prev
            del node
            return

        node.next.prev = node.prev
        node.prev.next = node.next
        del node

    def clean(self, asc):
        self.__ascending = asc
        node = self.head
        while node != None:
            delnode = node
            node = node.next
            del (delnode)
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        result = 0
        while node != None:
            result += 1
            node = node.next
        return result

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    def get_asc(self):
        return self.__ascending

    def set_asc(self, value):
        raise Exception("It is forbidden to change the asc attribute!")

    def del_asc(self):
        raise Exception("It is forbidden to delete the asc attribute!")

    asc = property(get_asc, set_asc, del_asc)



class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if v1.strip() < v2.strip(): 
            return -1
        if v1.strip() == v2.strip(): 
            return 0
        if v1.strip() > v2.strip(): 
            return 1
