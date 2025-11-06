'''
Given the head of a linked list, return the list after sorting it in ascending order.
'''

'''
approach 1=
convert linked list to array 
sort array 
convert array to linked list 

Time: O(nlogn)
Space: O(n)

approach 2=
divide and sort approach 

recursively divide until single node left
merge 

Time: O(nlogn)
Space: O(1)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, lst1, lst2):
        curr = ListNode(0)
        dummy = curr
        while lst1 and lst2:
            if lst1.val <= lst2.val:
                curr.next = lst1
                lst1 = lst1.next
            else:
                curr.next = lst2
                lst2 = lst2.next
            curr = curr.next
        curr.next = lst1 or lst2
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        lft = self.sortList(head)
        rht = self.sortList(mid)
        return self.merge(lft, rht)