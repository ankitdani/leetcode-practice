'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''

'''
Can k be invalid in any case ?
Can the tree be empty ?
'''

'''
Approach 1 : add all elements in array inorder and get kth element. O(n)

Approach 2 : early return 
The k-th smallest value will be found after k dfs inorder
decrement k after each recursive call
when k == 0 then the current node is the kth smallest node
'''

'''
1
|   |
2   3
    |   |
    4   5

k = 3
1,2,3,4,5
3rd smallest => 3
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
        self.counter = 0
        self.result = 0
        
    def helper (self, root, k):
        if not root:
            return 
        self.helper (root.left, k)

        self.counter += 1
        if self.counter == k:
            self.result = root.val
            return 

        self.helper (root.right, k)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.helper (root, k)
        return self.result