# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # if not root:
        #     return
        #
        # def helper(root, t):
        #     if not root:
        #         return t
        #     t = helper(root.right, t)
        #     root.val += t
        #     t = helper(root.left, root.val)
        #     return t
        # helper(root, 0)
        # return root
        self.sum = 0

        def dfs(root):
            if not root: return root
            dfs(root.right)
            self.sum = self.sum + root.val
            root.val = self.sum
            dfs(root.left)
            return root

        return dfs(root)
