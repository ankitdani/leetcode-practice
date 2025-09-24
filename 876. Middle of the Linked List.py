# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        odd
        1 -> 2 -> 3 -> 4 -> 5
        ||
        1 -> 2 -> 3 -> 4 -> 5
             |    |
        1 -> 2 -> 3 -> 4 -> 5
                  |         |

        even 
        1 -> 2 -> 3 -> 4 -> 5 -> 6
        ||
        1 -> 2 -> 3 -> 4 -> 5 -> 6
             |    |
        1 -> 2 -> 3 -> 4 -> 5 -> 6
                  |         |
        1 -> 2 -> 3 -> 4 -> 5 -> 6
                       |         |

        Time: O(n)
        Space: O(1)
        '''
        # if only head in list
        # loop until fast and fast.next is not null
        # return slow

        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow