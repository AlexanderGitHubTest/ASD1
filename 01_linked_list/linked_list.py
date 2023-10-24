"""
Linked list. 
"""

class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

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
        previous_node = None
        while node != None:
            if node.value == val:
                # delete node
                if previous_node == None:
                    self.head = node.next
                else:
                    previous_node.next = node.next
                if node.next == None:
                    self.tail = previous_node
                delnode = node
                node = node.next
                del(delnode)
                if not all: break
            else:
                previous_node = node
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
            else:
                newNode.next = self.head
                self.head = newNode
        else:
            while node != None:
                if node == afterNode:
                    # insert node
                    newNode.next = node.next
                    node.next = newNode
                    if newNode.next is None:
                        self.tail = newNode
                    break
                node = node.next
