# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         pre = None
#         cur = head
#
#         while cur:
#             t = cur.next
#             cur.next = pre
#             pre = cur
#             cur = t
#
#         return pre


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        t = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return t