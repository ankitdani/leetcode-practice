'''
Given the root of a binary tree, invert the tree, and return its root.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    '''
    Can the tree be empty ?
    '''

    '''
    11
    |           |
    -1          21
    |   |       |    |
    0   5       15   23

    11
    |           |
    -1          21
    |   |       |    |
    5   0       23   15

    11
    |           |
    21          -1
    |   |       |    |
    5   0       23   15
    '''

    '''
    if root null then return root
    each recursion will exchange left and right nodes
    '''

    '''
    Time: O(n)
    Space: O(1)
    '''

    def helper (self, root):
        if not root:
            return 
        root.left, root.right = root.right, root.left
        self.helper (root.left)
        self.helper (root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.helper (root)
        return root