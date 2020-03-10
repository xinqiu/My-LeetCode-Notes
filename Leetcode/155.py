class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        t = self.stack[-1]
        self.stack = self.stack[:-1]
        return t

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)

# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.data = []
#         self.min = None
#
#     def push(self, x):
#         if self.min == None or x <= self.min:
#             self.data.append(self.min)
#             self.min = x
#         self.data.append(x)
#
#     def pop(self):
#         if self.data.pop() == self.min:
#             self.min = self.data.pop()
#
#     def top(self):
#         return self.data[-1]
#
#     def getMin(self):
#         return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()