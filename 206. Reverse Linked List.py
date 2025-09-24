'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Can the list be empty ?
        '''

        '''
        1 -> 2 
        prev, curr, nxt, curr.next
        null, 1, 2, 2

        1 -> 2 
        after loop 1 =>
        prev, curr, nxt, curr.next
        1, 2, null, 1
        
        '''

        '''
        create a previous node 
        store next node in temp variable
        point next of current as previous
        set previous as current node
        move next node as current node 
        repeat until curr is null
        '''

        '''
        Time: O(n)
        Space: O(1)
        '''
        # case when head is null
        # iterate
        # return previous
        if not head:
            return head
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
