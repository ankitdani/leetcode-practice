'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
'''

'''
Can the tree be empty ?
What if 2 paths have same max sum ?
'''

'''
1
|    |
-2   3

max_sum = 4
'''

'''
at each recursion call, track max_sum globally = max(root + left_sum + right+sum)
for reach call return max(left_sum, right_sum, root.val)
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
    def __init__ (self):
        self.max_sum = float('-inf')

    def helper (self, root):
        if not root:
            return 0
        left_sum = max(0, self.helper (root.left))
        right_sum = max(0, self.helper (root.right))
        self.max_sum = max(self.max_sum, left_sum + right_sum + root.val)
        return max(left_sum, right_sum) + root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.helper (root)
        return self.max_sum