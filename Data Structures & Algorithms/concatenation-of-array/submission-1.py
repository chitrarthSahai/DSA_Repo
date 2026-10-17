class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #initialize array of twice length
        ans = [0] * 2 * n

        for i in range(n):
            #for each value in input array, put the same value in ans[i] and also ans[n+i], i.e. the supplement.
            ans[n + i] = ans[i] = nums[i]

        return ans