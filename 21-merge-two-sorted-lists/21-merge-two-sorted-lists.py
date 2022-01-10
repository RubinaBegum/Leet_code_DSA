class Solution(object):
    def mergeTwoLists(self, list1, list2):

        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        if list1.val <= list2.val:
            list_1 = list1
            list_2 = list2
        else:
            list_1 = list2
            list_2 = list1
        self.head = list_1
        
        current_1 = list_1
        head_2 = list_2
        current_2 = head_2
        
        stop = False
        while stop == False:
            if current_1.next == None:
                current_1.next = head_2
                stop = True
            elif head_2 == None:
                stop = True
            else:
                if current_1.next.val <= head_2.val:
                    current_1 = current_1.next
                else:
                    current_2 = current_2.next
                    head_2.next = current_1.next
                    current_1.next = head_2
                    current_1 = current_1.next
                    head_2 = current_2
        return self.head