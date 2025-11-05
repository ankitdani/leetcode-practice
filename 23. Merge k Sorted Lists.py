'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
'''

'''
[[1,3],[2,3],[5,6]]
[1,2,3,3],[5,6]
[1,2,3,3,5,6]

brute force
merge 2 lists at a time

Time: O(n*k), k = number of merges
Space: O(1)

approach 2 = 
use min heap

Time: O(n log k)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if not lists:
#             return None
#         merged = lists[0]
#         for i in range(1, len(lists)):
#             lst1 = merged
#             lst2 = lists[i]
#             head2 = ListNode(0)
#             dummy2 = head2
#             while lst1 and lst2:
#                 if lst1.val <= lst2.val:
#                     head2.next = lst1
#                     lst1 = lst1.next
#                 else:
#                     head2.next = lst2
#                     lst2 = lst2.next
#                 head2 = head2.next
#             head2.next = lst1 or lst2
#             merged = dummy2.next
#         return merged

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = ListNode(0)
        head = dummy
        while heap:
            _, idx, node = heapq.heappop(heap)
            head.next = node
            head = head.next
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        return dummy.next