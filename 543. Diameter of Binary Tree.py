'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
'''

'''
Can the tree be empty ?
'''

'''
1
|                   |
2                   3
|       |
4       5
|       |       |
-1      null    7
                |   
                9
'''

'''
Time: O(n)
Space: O(1)
'''

'''
recursion
at each level, track and return max of left height and right height
keep track globally of (left+right)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_till_now = 0

    def helper (self, root):
        if not root:
            return 0
        lft_ht = self.helper (root.left)
        rht_ht = self.helper (root.right)
        self.max_till_now = max(self.max_till_now, lft_ht + rht_ht)
        return 1 + max(lft_ht, rht_ht)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.helper (root)
        return self.max_till_now