from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)

        highestSequence = 0

        for nums in hash:
            print(nums)
            current_number = nums
            if current_number -1 not in hash:
                highestSequenceRun = 1
                
                while current_number+1 in hash:
                    highestSequenceRun += 1
                    current_number += 1
                
                if highestSequenceRun > highestSequence:
                    highestSequence = highestSequenceRun
            
        
        return highestSequence