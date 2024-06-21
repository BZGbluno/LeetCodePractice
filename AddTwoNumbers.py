# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Understand: I plan on having a variable to account for plus 1, and then moving forward
through the list
Match: Having 2 pointer for the list 
Plan:
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        addOne = False
        listOneComplete = False
        listTwoComplete = False
        CombinedList = ListNode()
        head = CombinedList
        first = l1
        second = l2


        while first or second:
            if first is None:
                listOneComplete = True
            if second is None:
                listTwoComplete = True

            if listOneComplete == False and listTwoComplete == False:
                value = first.val + second.val
                value, addOne = self.insertValue(value, addOne)
                first = first.next
                second = second.next
                
            elif listOneComplete == False:
                value = first.val
                value, addOne = self.insertValue(value, addOne)
                first = first.next
            else:
                value = second.val
                value, addOne = self.insertValue(value, addOne)
                second = second.next
            
            CombinedList.val = value
            if first or second:
                CombinedList.next = ListNode()
            if first is None and second is None and addOne:
                CombinedList.next = ListNode(1, None)

            CombinedList = CombinedList.next
        return head
            
        





    def insertValue(self, value, addOne):
        if addOne:
            value += 1
        if value >= 10:
            value = value % 10
            addOne = True
        else:

            addOne = False
        
        return value, addOne
