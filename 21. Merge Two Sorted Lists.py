'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Can a list be empty ?
        Can the list contain duplicates ?
        '''

        '''
        dummy 
        new head
        iterate new head
        if any list ends, point new head to other list
        '''

        '''
        Time: O(max(m,n))
        Space: O(1)
        '''

        dummy = ListNode(0)
        new_head = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                new_head.next = list1
                list1 = list1.next
            else:
                new_head.next = list2
                list2 = list2.next
            new_head = new_head.next
        if list1:
            new_head.next = list1
        else:
            new_head.next = list2
        return dummy.next
            
