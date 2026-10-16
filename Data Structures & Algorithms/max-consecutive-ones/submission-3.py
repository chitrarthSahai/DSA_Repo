class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)

        count, max_count = 0, 0
        for i in range(n):
            if nums[i] == 0:
                max_count = max(max_count, count)
                count = 0
            else:
                count += 1

            max_count = max(max_count, count)
        
        return max_count