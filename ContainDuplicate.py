class Solution:

    '''
    Understand: The worst case would be O(n) because it has to go through all the the points. We want to return true if   
    there are any doubles meaning we should break out of the loop once we encounter our first duplicate
    Match: We can use a hash set to store new numbers and once an duplicate appears if one does then we return true 
    Plan: Go through the array list and add to the hash set if it is not in it, if it is return true
    Implement
    Review 
    Evaluate
    '''

    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            else:
                numSet.add(num)
        return False