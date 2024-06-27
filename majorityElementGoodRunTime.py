class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Understand: This will be my O(n) space complexity solution with O(n) runt time
        Match: I will make a hashmap and count use the keys as the element and the value 
        as the number of times it is repeated
        Plan: I will traverse the values in the dictionary and return the one with the highest value
        """

        map = {}
        for element in nums:
            if element in map.keys():
                map[element] += 1
            else:
                map[element] = 1



        highest = 0
        for key in map.keys():
            print(map[key])
            print(highest)
            if int(map[key]) > int(highest):
                highest = map[key]
                value = key
        print(map)
        return value