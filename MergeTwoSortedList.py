# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        curr = head

        curr1 = list1
        curr2 = list2

        while (curr1 != None or curr2 != None):
            
            if (curr1 == None):
                self.fillRest(curr2, curr)
                break
            elif (curr2 == None):
                self.fillRest(curr1, curr)
                break

            else:
                if curr1.val < curr2.val:
                    curr.next = curr1
                    curr = curr.next
                    curr1 = curr1.next
                else:
                    curr.next = curr2
                    curr = curr.next
                    curr2 = curr2.next
        return head.next


    def fillRest(self, nonEmptyList, combinedList):
        while nonEmptyList != None:
            combinedList.next = nonEmptyList
            combinedList = combinedList.next
            nonEmptyList = nonEmptyList.next

