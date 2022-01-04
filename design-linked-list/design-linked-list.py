
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.sentinel = ListNode()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def get(self, index):
        current = self.sentinel
        for i in range(index+1):
            current = current.next
            if current == self.sentinel:
                return -1
        return current.val

    def addAtHead(self, val):
        current_head = self.sentinel.next
        new_head = ListNode(val)
        self.sentinel.next = new_head
        new_head.prev = self.sentinel
        new_head.next = current_head
        current_head.prev = new_head

    def addAtTail(self, val):
        current_tail = self.sentinel.prev
        new_tail = ListNode(val)
        self.sentinel.prev = new_tail
        new_tail.next = self.sentinel
        new_tail.prev = current_tail
        current_tail.next = new_tail

    def addAtIndex(self, index, val):
        current = self.sentinel
        for i in range(index):
            current = current.next
            if current == self.sentinel:
                return
        next_node = current.next
        new_node = ListNode(val)
        current.next = new_node
        new_node.prev = current
        new_node.next = next_node
        next_node.prev = new_node

    def deleteAtIndex(self, index):
        current = self.sentinel
        for i in range(index+1):
            current = current.next
            if current == self.sentinel:
                return
        prev_node, next_node = current.prev, current.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del current

    def getList(self):
        current = self.sentinel.next
        out = []
        while current != self.sentinel:
            out.append(current.val)
            current = current.next
        return out