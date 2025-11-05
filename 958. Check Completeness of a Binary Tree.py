'''
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
'''

'''
track 1st missing child using a flag.
if node is 1st seen as none, mark flag as true
if next time we see a node and flag is true then return false

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
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        que = deque()
        que.append(root)
        missing_child = False
        while que:
            curr = que.popleft()
            if curr:
                if missing_child:
                    return False
                que.append(curr.left)
                que.append(curr.right)
            else:
                missing_child = True
        return True