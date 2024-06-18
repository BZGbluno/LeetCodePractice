# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Understand: reverse the nodes within left and right inclusive
Match: I plan on splitting this into 3 linked list, Prior to reverse, reverse, and after reverse.
Then I will combine
Plan:
1 > 2 > 3 > 4 > 5 for 2,4
1) 1 > None
2) 5 > None
3) Call reverse so then 4 > 3 > 2
4) 1 > 4 > 3 > 2> 5

'''
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = head
        amountOfTimes = right-left + 1
        if left > 1:
            for x in range(0, left-2):
                current = current.next


            priorToReverse = current
            print(priorToReverse)
            ReverseList = current.next
            print(ReverseList)
            reversedList = self.reverse(ReverseList, amountOfTimes)
            priorToReverse.next = reversedList
        else:
            ReverseList = current
            reversedList = self.reverse(ReverseList, amountOfTimes)
            return reversedList



        # amountOfTimes = right-left + 1
        # reversedList = self.reverse(ReverseList, amountOfTimes)



        # priorToReverse.next = reversedList
        return head


    def reverse(self, begin, amountOfTimes):
        
        current = begin
        prev = None
        nextNode = None
        x = 0
        lastNode = None
        connect = None
        while current and x < amountOfTimes:
            
            nextNode = current.next
            current.next = prev
            prev = current
            if(x == 0):
                connect = prev
                print(connect.val)
            current = nextNode
            x += 1
            print(f'{x} and {connect.val}')
            if(x == amountOfTimes):
                connect.next = current
        

        return prev
