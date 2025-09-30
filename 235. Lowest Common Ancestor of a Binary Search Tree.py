'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''

'''
Can the input be invalid in any case ?
'''

'''
recursion
compare root value with p and q
if greater move to left subtree
else if traverse right subtree
else root is the lca
'''

'''
1
|   |
2   3
    |   |
    4   5

p = 4, q = 5
'''

'''
Time: O(log n)
Space: O(log n) => log n function calls, calls in stack take memory
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            self.lowestCommonAncestor(root.right, p, q)
        return root