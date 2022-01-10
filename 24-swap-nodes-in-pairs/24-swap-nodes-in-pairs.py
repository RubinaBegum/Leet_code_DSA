# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        cdr = head.next
        if cdr is None:
            return head
        new_next = self.swapPairs(cdr.next)
        head.next = new_next
        cdr.next = head
        return cdr