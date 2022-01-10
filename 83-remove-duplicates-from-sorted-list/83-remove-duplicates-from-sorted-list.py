
class Solution(object):
    def deleteDuplicates(self, head):
        temp = ListNode(-101)
        temp.next=head
        head = temp
        while True:
            if temp is None or temp.next is None:
                break
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head.next
