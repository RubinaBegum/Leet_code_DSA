# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        s = set()
        itr = headA
        
        while itr:
            s.add(itr)
            itr = itr.next
        
        itr = headB
        while itr:
            if itr in s:
                return itr
            itr = itr.next
        return itr
        