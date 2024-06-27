from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        '''
        Understand: Every location has sometype of destination no matter where I start  
        Mathc: Use a hashmap, use the keys to be the airport and the value is the destination
        PLan: Loop of adding into the dictionary and if something value is an existing key the keep searching
        until no more destinations exist
        '''



        hashMap = dict(paths)
        print(hashMap)

        dest = paths[0][1]
        while dest in hashMap:
            dest = hashMap[dest]
            print(dest)

        return dest