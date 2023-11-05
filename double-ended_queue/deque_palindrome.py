"""
Function that determines whether a phrase is a palindrome.
"""

from deque import Deque


def deque_palindrome(string):
    deq = Deque()
    for  char in string:
        if char.isalpha():
            deq.addTail(char.lower())
    if deq.size() == 0:
        raise Exception("Phrase is empty!")
    while deq.size() > 1:
        if deq.removeFront() != deq.removeTail():
            return False
    return True
