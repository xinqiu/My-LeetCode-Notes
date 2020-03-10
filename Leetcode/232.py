class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.count = 0
        self.front = None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.count += 1
        self.queue.append(x)
        if self.count == 1:
            self.front = x



    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        t = []

        for _ in range(self.count):
            t.append(self.queue.pop())
        ret = t.pop()
        if len(t) != 0:
            self.front = t[-1]
        else:
            self.front = None

        self.count -= 1
        for _ in range(self.count):
            self.queue.append(t.pop())
        return ret


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.front

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.count == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()