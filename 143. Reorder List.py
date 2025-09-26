'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        '''
        Can the head be null ?
        Can the list have duplicate values ?
        Can all values of a list be same ?
        '''
        
        '''
        break the list in half
        reverse 2nd half of list
        alternately point to 1st and 2nd list
        if any list exhausts then point new_head to the other list
        '''

        '''
        Time: O(n)
        Space: O(1)
        '''

        '''
        1 -> 2 -> 3 -> 4

        1 -> 2 -> null
        3 -> 4 -> null

        1 -> 2 -> null
        4 -> 3 -> null

        1 -> 4 -> 2 -> 3 -> null
        '''

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None

        reversed_head2 = self.reverse(head2)

        dummy = ListNode(-1)
        curr = ListNode(-1)
        dummy.next = curr
        while head and reversed_head2:
            curr.next = head
            head = head.next

            curr = curr.next

            curr.next = reversed_head2
            reversed_head2 = reversed_head2.next

            curr = curr.next
        
        if head:
            curr.next = head
        else:
            curr.next = reversed_head2

        return dummy.next
    
    def reverse (self, head2):
        curr = head2
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        