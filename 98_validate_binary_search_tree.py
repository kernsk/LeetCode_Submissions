# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Input:    a TreeNode (root of a binary tree)
# Task:     determine if it is a valid binary tree
# Valid:    the left subtree of a node only contains nodes with keys less than its key
#           the right subtree of a node only contains nodes with keys greater than its key
#           both the left and right subtrees must also be binary search trees
# Output:   a boolean

from collections import deque

class Solution:
    def __init__(self):
        self.visited = []

    def inOrder(self, node):
        if node == None:
            return
        self.inOrder(node.left)
        self.visited.append(node.val)
        self.inOrder(node.right)
        
    def validate(self, node):
        self.inOrder(node)
        if len(self.visited) == 1:
            return True
        
        for i in range(1, len(self.visited)):
            if self.visited[i-1] >= self.visited[i]:
                return False
        return True


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root)