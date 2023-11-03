"""
Function that "rotates" the queue in a circle of N elements.
"""

from collections import deque

from queue import Queue


def queue_rotate(queue, n):
    if queue.size() < 2:
        return   
    n = n % queue.size()
    for _ in range(n):
            queue.enqueue(queue.dequeue())
