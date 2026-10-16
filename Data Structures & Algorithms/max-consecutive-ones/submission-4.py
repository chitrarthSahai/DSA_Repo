class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #Most optimized approach

        count = max_count = 0

        for num in nums:
            count = count + 1 if num else 0
            max_count = max(max_count, count)
        
        return max_count