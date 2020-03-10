# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
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


'''
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def helper(node, level):
            if not node:
                return
            else:
                ret[level-1].append(node.val)
                if len(ret) == level:  # 遍历到新层时，只有最左边的结点使得等式成立
                    ret.append([])
                helper(node.left, level+1)
                helper(node.right, level+1)
        ret = [[]]
        helper(root, 1)
        return ret[:-1]
'''

'''
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        T = [root]
        while T and root:
            ret.append([x.val for x in T])
            T = [p for n in T for p in (n.left, n.right) if p]
        return ret
'''