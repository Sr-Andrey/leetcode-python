"""Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself."""

"""Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    SEP = "|"
    NULL = "N"

    def serialize_preorder(self, root) -> list[str]:
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node is None:
                res.append(self.NULL)
                continue
            res.append(str(node.val))
            stack.append(node.right)
            stack.append(node.left)
        return res

    def read_preorder(self, values: list[str]) -> Optional[TreeNode]:
        val = values.pop()
        if val == self.NULL:
            return None
        node = TreeNode(int(val))
        node.left = self.read_preorder(values)
        node.right = self.read_preorder(values)
        return node


    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.SEP.join(self.serialize_preorder(root))


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        values = data.split(self.SEP)
        values.reverse()
        return self.read_preorder(values)
