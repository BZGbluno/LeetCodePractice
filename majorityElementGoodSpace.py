class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Understand: This will be my O(1) space complexity solution with O(nlogn) runt time
        Match: I will be only re arranging the array by sorting it in ascending order
        Plan: I will sort the array. If the item occurs more than n/2 times then if we 
        retrieve the center element than we should be able to return the majority element
        """


        nums.sort()
        return nums[len(nums)/2]