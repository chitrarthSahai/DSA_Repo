class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #initialize array of twice length. bracket is important, other wise it will intialze and array of [0][0] n times, instead [0] 2n times. Python won't complain because lists are dynamic array, but it will take time to find memory and fill those extras indexes.
        ans = [0] * (2 * n)

        for i in range(n):
            #for each value in input array, put the same value in ans[i] and also ans[n+i], i.e. the supplement.
            ans[n + i] = ans[i] = nums[i]

        return ans