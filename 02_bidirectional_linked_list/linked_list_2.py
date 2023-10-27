"""
Linked list 2. 
"""

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        result = []
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        node = self.head
        while node != None:
            if node.value == val:
                # delete node
                if node.prev == None:
                    if node.next is None:
                        self.head = None
                        self.tail = None                
                    else:
                        self.head = node.next
                        node.next.prev = None
                else:
                    if node.next is None:
                        self.tail = node.prev
                        node.prev.next = None
                    else:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                delnode = node
                node = node.next
                del(delnode)
                if not all: break
            else:
                node = node.next

    def clean(self):
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

    def insert(self, afterNode, newNode):
        node = self.head
        if afterNode is None:
            if node is None:
                self.head = newNode
                self.tail = newNode
                newNode.next = None
                newNode.prev = None
            else:
                while node.next != None:
                    node = node.next
                self.tail = newNode
                node.next = newNode
                newNode.prev = node
                newNode.next = None
        else:
            while node != None:
                if node == afterNode:
                    # insert node
                    newNode.next = node.next
                    newNode.prev = node
                    node.next = newNode
                    if newNode.next is None:
                        self.tail = newNode
                    else:
                        newNode.next.prev = newNode
                    break
                node = node.next

    def add_in_head(self, newNode):
        if self.head is None:
            self.tail = newNode
            newNode.next = None
        else:
            self.head.prev = newNode
            newNode.next = self.head
        newNode.prev = None
        self.head = newNode
