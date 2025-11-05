'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
'''

'''
serialize=
convert treenode value into string
add it to string array
concat with ,
use bfs and queue

deserialize=
use queue
1st element = root
if element is not null then append node to queue, and assign to root.left
if element is not null then append node to queue, and assign to root.right

Time: O(n)
Space: O(n)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serial = []
        que = deque([root])
        while que:
            node = que.popleft()
            if node:
                serial.append(str(node.val))
                que.append(node.left)
                que.append(node.right)
            else:
                serial.append("null")
        return ",".join(serial)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(",")
        
        if data[0] == "null":
            return None
        root = TreeNode(int(data[0]))
        i = 1
        que = deque([root])
        while que and i < len(data):
            curr = que.popleft()
            if i < len(data) and data[i] != "null":
                curr.left = TreeNode(int(data[i]))
                que.append(curr.left)
            i += 1
            if i < len(data) and data[i] != "null":
                curr.right = TreeNode(int(data[i]))
                que.append(curr.right)
            i += 1
            
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))