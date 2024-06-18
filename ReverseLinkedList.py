# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
Understand: We need to reverse the linked list meaning we need move the pointers from right to left,
when doing this you are going to split the linked list into 2 where u are adding backwards to one of them
Match: I plan of having 1 pointer to the current, then 1 to the prev and add to the prev by adding to its head
Plan: 1 > 2 > 3 > None
1) 1> None and 2 > 3>  None
2) 2 > 1 > None and 3 > None
3) 3 > 2 > 1 > None and None
'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        nextNode = None
        current = head
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
            
            
        return prev
