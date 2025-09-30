'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''

'''
1                       1
|   |                   |   |
2   3                   2   3
'''

'''
Can 1 of the trees be empty?
'''

'''
recursion
if we reach the end of the tree then return true
invalid conditions are value not same, 1 of the node is null
'''

'''
Time: O(m+n)
Space: O(1)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (not p and q) or (p.val != q.val):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)