'''
Given a binary tree, determine if it is height-balanced.
'''

'''
What does height balance mean? - difference between 2 levels is never greater than 1
Can the tree be empty ?
'''

'''
recursion
in each call track left, right height and diff
return left height and right height and the diff at every function call
'''

'''
1
|           |
2           3
|       |
4       5
|
6
|   |
7   8
'''

'''
Time: O(n)
Space: O(h)
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
            return [True, 0]
        left = self.helper(root.left)
        right = self.helper(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balanced, 1 + max(left[1], right[1])]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper (root)[0]
