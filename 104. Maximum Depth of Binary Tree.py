'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

'''
Can the tree be empty ?
'''

'''
1
|               |
2               3
|      |
null   4
'''

'''
recursion 
at every level track max depth +1
'''

'''
Time: O(n)
Space: O(1)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper (self, root):
        if not root:
            return 0
        return max(self.helper(root.left), self.helper(root.right)) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.helper (root)