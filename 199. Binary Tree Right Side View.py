'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''

'''
1
|   |
2   3
    |   |
    4   5

result => 1,3,5

Q = 1

current = 1
result = 1
Q = 2,3

current = 2
result = 1
Q = 3

current = 3
result = 1,3
Q = 4,5

current = 4
result = 1,3
Q = 5

current = 5
result = 1,3,5
Q = null
'''

'''
traverse level wise
whenever it is the last element in the level , add it to the result
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
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            size = len(queue)
            for i in range(size):
                curr_node = queue.popleft()
                if i == size-1:
                    result.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return result