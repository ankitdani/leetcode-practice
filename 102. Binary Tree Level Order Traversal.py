'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''

'''
Can the tree be empty?
'''

'''
use a queue
initialize the queue with root
In each iteration, we pop a node, add it to the result and add its children to queue
'''

'''
1
|   |
2   3
    |   |
    4   5

1,2,3,4,5
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = deque()
        queue.append(root)
        while queue:
            lst = []
            size = len(queue)
            for _ in range(size):
                curr_node = queue.popleft()
                lst.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            result.append(lst)
        return result
