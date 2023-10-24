"""
Linked List - additional task
"""

from linked_list import LinkedList, Node

def add_two_linked_lists(LL1, LL2):
    """
    Function returns a linked list, each element of which is the sum of the corresponding elements of the input linked lists. 
    Length of lists must equal.
    """
    if LL1.len() != LL2.len(): 
        raise Exception("The length of the linked lists is not the same!")
    
    LL_return = LinkedList()

    node1 = LL1.head
    node2 = LL2.head
    while node1 != None:
        LL_return.add_in_tail(Node(node1.value + node2.value))
        node1 = node1.next
        node2 = node2.next

    return LL_return