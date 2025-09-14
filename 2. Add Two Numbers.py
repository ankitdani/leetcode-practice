class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def add_two_numbers (self, l1, l2):
        dummy = ListNode(0)
        lst = dummy
        carry = 0
        lst1 = l1
        lst2 = l2
        while lst1 or lst2 or carry != 0:
            num1 = lst1.val if lst1 else 0
            num2 = lst2.val if lst2 else 0
            sum = num1 + num2 + carry
            lst.next = ListNode(sum % 10)
            carry = sum // 10
            lst1 = lst1.next if lst1 else None
            lst2 = lst2.next if lst2 else None
        if carry:
            lst.next = ListNode(carry)
        return dummy.next