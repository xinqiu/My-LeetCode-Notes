import Queue

class MaxQueue(object):

    def __init__(self):
        self.deque = Queue.deque()
        self.m = -1


    def max_value(self):
        """
        :rtype: int
        """
        return self.m if self.deque else -1



    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.m = max(value, self.m)
        self.deque.append(value)


    def pop_front(self):
        """
        :rtype: int
        """
        if not self.deque:
            return -1
        ret = self.deque.popleft()
        if ret == self.m:
            self.m = max(self.deque) if self.deque else -1
        return ret


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()