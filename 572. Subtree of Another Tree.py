'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
'''

'''
1                       3
|   |                   |   |
2   3                   4   5
    |   |
    4   5
'''

'''
Can any tree be empty ?
'''

'''
check if every node in main tree is the root of subtree
if it is then check all nodes if they are same
'''

'''
Time: O(m.n)
Space: O(h1+h2)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper (self, root, subRoot):
        if not root and not subRoot:
            return True
        if (not root and subRoot) or (root and not subRoot) or (root.val != subRoot.val):
            return False
        return self.helper(root.left, subRoot.left) and self.helper(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (not root and subRoot) or (root and not subRoot):
            return False
        if (root.val == subRoot.val):
            if(self.helper(root, subRoot)):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)