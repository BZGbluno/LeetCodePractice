class Solution:
    '''
    In this solution you only swap the length of the word dvided by 2. For cases that are odd, we do
    integer division because we don't need to swap the center letter of an odd length. This solution is
    O(1) for space complexity because we only use pointers, and it is O(n) where n is half of the length 
    of the total items
    '''
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        swaps = len(s)//2
        
        temp = None
        beginningPointer = 0
        endPointer = len(s)-1

        for x in range(0, swaps):
            temp = s[beginningPointer]
            s[beginningPointer] = s[endPointer]
            s[endPointer] = temp
            beginningPointer += 1
            endPointer -= 1
