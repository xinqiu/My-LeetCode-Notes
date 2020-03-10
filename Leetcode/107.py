# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        ret = []
        queue = [root]

        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.pop(0)
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(current_level)

        return ret


"""
class Solution(object):
    def levelOrderBottom(self, root):
        ret = []
        T = [root]
        while T and root:
            ret.insert(0,[x.val for x in T])
            T = [p for n in T for p in (n.left, n.right) if p]
        return ret
"""

solution = Solution()

A = TreeNode(1)
B = TreeNode(3)
C = TreeNode(2)
D = TreeNode(4)

A.left = B
A.right = C
C.left = D

print solution.levelOrderBottom(A)