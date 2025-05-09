# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.


# Definition for a Node.
from typing import Optional


import collections
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    """
    This class provides a solution to copy a linked list with random pointers.
    It uses a hash map (dictionary in Python) to store the mapping between 
    nodes in the original list and their corresponding nodes in the new list.
    This allows for efficient lookup when setting the random pointers.
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}
        
        curr = head
        
        while curr:
            new_node = Node(curr.val)
            old_to_new[curr] = new_node
            curr = curr.next
        
        curr = head
        
        while curr:
            new_node = old_to_new[curr]
            
            if curr.next:
                new_node.next = old_to_new[curr.next]
            else:
                new_node.next = None
                
            if curr.random:
                new_node.random = old_to_new[curr.random]
            else:
                new_node.random = None
            
            curr = curr.next
        
        return old_to_new[head]
                
            