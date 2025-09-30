'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''

'''
Can the tree be empty ?
Confirm definition of good nodes
'''

'''
1
|   |
2   3
    |   |
    4   1

good nodes = 3 (2,3,4)
'''

'''
recursion
track max value till now
if current node value >= max seen so far then increment result
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
    def __init__(self):
        self.good_nodes = 0

    def helper (self, root, max_so_far):
        if not root:
            return 0
        if root.val >= max_so_far:
            self.good_nodes += 1
            max_so_far = root.val
        self.helper(root.left, max_so_far)
        self.helper(root.right, max_so_far)

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.helper (root, root.val)
        return self.good_nodes