# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        node = ListNode(None)
        node.next = head
        p = node
        while p.next:
            if p.next.val != val:
                p = p.next
            else:
                p.next = p.next.next
        return node.next