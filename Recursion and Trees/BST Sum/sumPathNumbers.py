"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers.

A leaf node is a node with no children.

"""
from node import TreeNode

def sumPathNumbersHelper(root,currSum):
    # currSum = 0
    if root is None:
        return 0
    currSum = (currSum*10)+root.val
    if root.left is None and root.right is None:
        return currSum
    
    return (sumPathNumbersHelper(root.left,currSum)) +(sumPathNumbersHelper(root.right,currSum))
    
def sumPathNumbers(root):
    return sumPathNumbersHelper(root,0)

root = TreeNode(1, TreeNode(2), TreeNode(3))
print(sumPathNumbers(root))