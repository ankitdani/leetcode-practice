'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

'''
strictly = only greater than or less than right ?
Can the tree be empty ?
'''

'''
compare current node with lower limit and higher limit
if current node value out of bounds then return false
else traverse downwards
'''

'''
1
|   |
-1  3
    |   |
    2   4

current = 1

for left subtree =>
lower limit = -inf
higher limit = 1

for right subtree =>
lower limit = 1
higher limit = inf

current = -1

for left subtree =>
lower limit = -1
higher limit = 1

current = 2

for right subtree =>
lower limit = 1
higher limit = 3

current = 4

for right subtree =>
lower limit = 1
higher limit = 4
'''

'''
Time: O(n)
Space: O(n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper (self, root, lower_bound, upper_bound):
        if not root:
            return True
        if root.val <= lower_bound or root.val >= upper_bound:
            return False
        return self.helper(root.left, lower_bound, root.val) and self.helper(root.right, root.val, upper_bound)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if self.helper (root, float('-inf'), float('inf')):
            return True
        return False