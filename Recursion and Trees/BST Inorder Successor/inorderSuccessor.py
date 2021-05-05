"""
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.

Hint: Remember that the in-order traversal of a binary search tree is the nodes in sorted order.
"""

from node import TreeNode

def inorderSuccessor(root, p):
    if root is None or p is None:
        return None
    if root==p:
        if root.right is None:
            return None
        result = root.right
        while result.left is not None:
            result = result.left
        return result
    if root.val<p.val:
        return inorderSuccessor(root.right,p)
    return inorderSuccessor(root.left,p) or root

