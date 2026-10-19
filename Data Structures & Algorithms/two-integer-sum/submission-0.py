class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #BruteForce
        # Iterate over the array, for each iteration iterate over rest of the elements and add them and 
        # comapare them to the target, when found return i, j counters of that iteration

        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
                