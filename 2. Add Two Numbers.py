'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Can the list be empty ?
        Can the list contain duplicate values ?
        '''

        '''
        1 -> 2 -> 9
        9 -> 5 -> 5
        '''

        '''
        iterate both lists simultaneously  until both or 1 of the list if exhausted
        keep track of cary for each iteration and add to next iteration
        if carry at th end of both iterations then create a new node and add carry
        '''

        '''
        Time: O(n)
        Space: O(1)
        '''

        curr1 = l1
        curr2 = l2
        carry = 0
        dummy = ListNode(-1)
        curr = dummy
        dummy.next = curr
        while curr1 or curr2 or carry:
            num1 = curr1.val if curr1 else 0
            num2 = curr2.val if curr2 else 0
            sum = num1 + num2 + carry
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        return dummy.next
