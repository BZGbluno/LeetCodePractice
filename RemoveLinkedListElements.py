# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Understand: I have to remove any target values from the linked list. This can be done in O(n)
    run tiem and O(1) time complexity
    Match: I will be using a singly linked list
    Plan: I plan on going with a 2 pointer strategy, one will be previous and the second be the one
    that is checked against the value
    '''

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        curr = head.next
        prev = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else: 
                curr = curr.next 
                prev = prev.next

        # Check the head
        if head.val == val:
            return head.next
        return head
