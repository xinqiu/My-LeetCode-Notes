# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.depth(root) != -1

    def depth(self, root):
        if not root: return 0
        left = self.depth(root.left)
        if left == -1: return -1
        right = self.depth(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1
'''

'''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True
        def helper(root):
            if not root:
                return 0
            left = helper(root.left) + 1
            right = helper(root.right) + 1
            if abs(right - left) > 1: 
                self.res = False
                return 0
            return max(left, right)
        helper(root)
        return self.res
'''

class Solution(object):
    def depth(self, root):
        if root:
            return max(self.depth(root.left), self.depth(root.right))+1
        else:
            return False

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return abs(self.depth(root.right)-self.depth(root.left)) <= 1 and self.isBalanced(root.right) and self.isBalanced(root.left)
        else:
            return True
