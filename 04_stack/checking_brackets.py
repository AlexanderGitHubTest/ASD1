"""
Stack-based check whether the brackets in the string are balanced.
"""

from stack import Stack

def checking_brackets(string_to_check):
    stack = Stack()
    for char in string_to_check:
        if char == '(':
            stack.push('(')
        if char == ')' and stack.pop() != '(':
            return False
    return True if stack.size() == 0 else False
