'''
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        Can the list be empty ?
        What happens if all the random pointers are null ?
        Can multiple nodes have their random pointers pointing to the same node?
        Can random pointers self point ?
        '''

        '''
        1st pass = create a copy of all nodes in hashmap
        2nd pass = assign random and next pointers to copies
        return copy of head
        '''

        '''
        1 -> 2
        hashmap = null

        1 -> 2
        hashmap = 1 -> 1 copy
        1 copy.next -> null #TODO

        1 -> 2
        hashmap = 1 -> 1 copy, 2 -> 2 copy
        1 copy.next -> 2 copy, 2 copy.next = null
        '''

        '''
        Time: O(n)
        Space: O(n)
        '''

        if not head:
            return head

        curr = head
        hashmap = {}
        while curr:
            if curr not in hashmap:
                hashmap[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            hashmap[curr].next = hashmap.get(curr.next)
            hashmap[curr].random = hashmap.get(curr.random)
            curr = curr.next
        return hashmap[head]