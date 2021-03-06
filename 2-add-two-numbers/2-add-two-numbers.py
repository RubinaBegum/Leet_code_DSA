
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        num1 = str(l1.val)
        num2 = str(l2.val)
        while l1.next:
            l1 = l1.next
            num1 = str(l1.val) + num1
        while l2.next:
            l2 = l2.next
            num2 = str(l2.val) + num2
        num3 = list(str(int(num1) + int(num2)))

        n1 = ListNode(int(num3.pop(0)))
        n = n1
        while num3:
            n = ListNode(int(num3.pop(0)))
            n.next = n1
            n1 = n
        return n