class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Another approach is to early exit once a complement is found. Still needs 2 loops

        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            for j in range(i+1, n):
                if nums[j] == complement:
                    return [i,j]