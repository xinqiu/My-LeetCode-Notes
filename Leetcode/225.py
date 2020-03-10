from Queue import Queue

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = Queue()
        self.count = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack.put(x)
        self.count += 1
        self.top_element = x

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        t = Queue()
        for i in range(self.count-1):
            self.top_element = self.stack.get()
            t.put(self.top_element)
        ret = self.stack.get()
        self.count -= 1
        self.stack = t
        return ret

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.top_element

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.stack.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()