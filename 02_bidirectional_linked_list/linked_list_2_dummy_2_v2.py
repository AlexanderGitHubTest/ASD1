"""
Linked list 2 (+ 2 dummy nodes) v2 (removed the dummy attribute from the Node class). 
"""

class Node:
    def __init__(self, v):
        self.value = v
        self._prev = None
        self._next = None

    def get_prev(self):
        if isinstance(self._prev, NodeDummy):
            return None
        else:
            return self._prev

    prev = property(get_prev)

    def get_next(self):
        if isinstance(self._next, NodeDummy):
            return None
        else:
            return self._next

    next = property(get_next)

class NodeDummy(Node):
    pass      

class LinkedList2:  
    def __init__(self):
        self._head = NodeDummy(None)
        self._tail = NodeDummy(None)
        self._head._next = self._tail
        self._tail._prev = self._head

    def get_head(self):
        if isinstance(self._head._next, NodeDummy):
            return None
        else:
            return self._head._next

    head = property(get_head)

    def get_tail(self):
        if isinstance(self._tail._prev, NodeDummy):
            return None
        else:
            return self._tail._prev

    tail = property(get_tail)

    def add_in_tail(self, item):
        item._next = self._tail
        item._prev = self._tail._prev
        self._tail._prev._next = item
        self._tail._prev = item

    def find(self, val):
        node = self._head._next
        while not isinstance(node, NodeDummy):
            if node.value == val:
                return node
            node = node._next
        return None

    def find_all(self, val):
        node = self._head._next
        result = []
        while not isinstance(node, NodeDummy):
            if node.value == val:
                result.append(node)
            node = node._next
        return result

    def delete(self, val, all=False):
        node = self._head._next
        while not isinstance(node, NodeDummy):
            if node.value == val:
                node._prev._next = node._next
                node._next._prev = node._prev
                delnode = node
                node = node._next
                del(delnode)
                if not all: break
            else:
                node = node._next

    def clean(self):
        node = self._head._next
        while not isinstance(node, NodeDummy):
            delnode = node
            node = node._next
            del (delnode)
        self._head._next = self._tail
        self._tail._prev = self._head

    def len(self):
        node = self._head._next
        result = 0
        while not isinstance(node, NodeDummy):
            result += 1
            node = node._next
        return result

    def insert(self, afterNode, newNode):
        node = self._head._next
        if afterNode is None:
            if isinstance(node, NodeDummy):
                newNode._prev = self._head
                newNode._next = self._tail
                self._head._next = newNode
                self._tail._prev = newNode
            else:
                newNode._prev = self._tail._prev
                newNode._next = self._tail
                self._tail._prev._next = newNode
                self._tail._prev = newNode
        else:
            while not isinstance(node, NodeDummy):
                if node == afterNode:
                    newNode._prev = node
                    newNode._next = node._next
                    node._next._prev = newNode
                    node._next = newNode
                    break
                node = node._next

    def add_in_head(self, newNode):
        newNode._next = self._head._next
        newNode._prev = self._head
        self._head._next._prev = newNode
        self._head._next = newNode
