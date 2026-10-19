class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #The optimized approach is to maintain a hashmap with values and indices, we then find the complement in the map with O(1) complexity, if found and found index is not equal to current index (that is why we maintain the index in the map) we return that i and j, otherwise we insert the element and it's index

        hashmap = {}

        for idx, num in enumerate(nums):
            complement  = target - num
            if complement in hashmap and hashmap[complement] != idx:
                return [hashmap[complement], idx]
            else:
                hashmap[num] = idx

