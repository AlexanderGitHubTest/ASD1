"""
The function computes postfix expressions using two stacks.
(added operations '/' (Return a // b) and '-' (Return a - b))
"""

import operator

from stack import Stack

def calculate_postfix_expression(expression):
    dict = {'+': operator.add, '*': operator.mul, '-': operator.sub, '/': operator.floordiv}
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
            second_operand = int(stack2.pop())
            stack2.push(dict[obj](int(stack2.pop()), second_operand))
    raise Exception('Empty expression or missing "="!')
