# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Understand: I need to remove the nth last node, I need to worry about the edge cases
    which would be the beginning of the array. To Account for this, we make another listNode
    Match: I will be using 2 pointers since we are removing something that might not be at the
    beginning of the array
    Plan: I will traverse the array n+1 times because the one account for the added node and
    the goal is to start traversing a second pointer at the same time with th first ends meaning
    that the second pointer will stop one node before the nth node. We then remove that nth node
    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(val=0, next = head)


        first = temp
        second = temp
        for _ in range(n+1):
            first = first.next
        
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return temp.next
