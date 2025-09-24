'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Can the list be empty ?
        what if n > length of the list ?
        '''

        '''
        1 -> 2 -> 3 -> 4, n = 3
        remove 1st node from the end that is 2

        '''

        '''
        Approach 1 - calculate length of the list, length -n = node to be removed. drawbacks = iterating every node twice

        Approach 2 - distance between 2 pointers should be n
        iterate pointer 1 till n > 0
        initialise 2nd pointer to head
        move the 2nd and 1st pointer simultaneously till pointer1 is null
        by now the pointer2 will point to the previous of the node to be removed
        point to the next of the node to be removed
        '''

        '''
        Time: O(N+n)
        Space: O(1)
        '''

        dummy = ListNode(-1)
        dummy.next = head
        curr1 = dummy
        while n > 0:
            curr1 = curr1.next
            n -= 1
        curr2 = dummy
        while curr1.next:
            curr1 = curr1.next
            curr2 = curr2.next
        curr2.next = curr2.next.next if curr2.next else None
        return dummy.next