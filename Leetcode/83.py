# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        if not head or not head.next:
            return head
        while head:
            if head.next and head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return p