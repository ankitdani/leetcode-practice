'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
'''

'''
Can the tree be empty ?
'''

'''
preorder = [1,2,3,4], inorder = [2,1,4,3]

1
|   |
2   3
    |   
    4   
'''

'''
preorder = root,left,right
root of the tree found in preorder's 1st element
search root in inorder. In inorder, left of root is the left subtree and right part is the right subtree
recursively call until no elements left
'''

'''
Time: O(2n)
Space: O(2n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.preorder_index = 0

    def helper (self, preorder, inorder, inorder_map, start, end):
        if start > end:
            return None
        root = TreeNode(preorder[self.preorder_index])
        self.preorder_index += 1
        inorder_index = inorder_map[root.val]
        root.left = self.helper (preorder, inorder, inorder_map, start, inorder_index-1)
        root.right = self.helper (preorder, inorder, inorder_map, inorder_index+1, end)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i, num in enumerate(inorder):
            inorder_map[num] = i
        return self.helper (preorder, inorder, inorder_map, 0, len(preorder)-1)