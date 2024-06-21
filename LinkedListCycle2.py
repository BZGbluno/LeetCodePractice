# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cycle = self.cycleFinder(head)
        if cycle:
            current = head
    

            while current != cycle:
                current = current.next
                cycle = cycle.next
            return current
        
        return cycle





    def cycleFinder(self, head):
        if head is None:
            return None
        slowPointer = head
        fastPointer = head

        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

            if slowPointer == fastPointer:
                print(slowPointer.val)
                return fastPointer
        return None
