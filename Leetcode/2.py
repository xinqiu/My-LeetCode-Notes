# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = ''
        while l1 != None:
            n1 = str(l1.val) + n1
            l1 = l1.next

        n2 = ''
        while l2 != None:
            n2 = str(l2.val) + n2
            l2 = l2.next

        s = str(int(n1)+int(n2))[::-1]
        print(s)
        p = ListNode(int(s[0]))
        ret = p
        for c in s[1:]:
            p.next = ListNode(int(c))
            p = p.next
        return ret


solution = Solution()

l1 = ListNode(1)
l1.next = ListNode(8)

l2 = ListNode(0)

print(solution.addTwoNumbers(l1, l2))