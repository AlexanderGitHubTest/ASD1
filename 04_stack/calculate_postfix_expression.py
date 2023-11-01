"""
The function computes postfix expressions using two stacks.
"""

import operator

from stack import Stack

def calculate_postfix_expression(expression):
    dict = {'+': operator.add, '*': operator.mul}
    stack1 = Stack()
    stack2 = Stack()
    for obj in expression.split()[::-1]:
        stack1.push(obj)
    while stack1.size() > 0:
        obj = stack1.pop()
        if obj.isdigit():
            stack2.push(obj)
        elif obj == '=':
            return stack2.pop()
        elif stack2.size() <= 1:
            raise Exception('Incorrect expression!')
        else:
            stack2.push(dict[obj](int(stack2.pop()), int(stack2.pop())))
    raise Exception('Empty expression or missing "="!')
