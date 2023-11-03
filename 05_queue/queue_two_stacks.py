"""
Queue of two stacks.
"""

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        return None

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() > 0:
            return self.stack[-1]
        return None

class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.size() > 0:
            return self.stack2.pop()
        while self.stack1.size() > 1:
            self.stack2.push(self.stack1.pop())
        return self.stack1.pop()

    def size(self):
        return self.stack1.size() + self.stack2.size()
