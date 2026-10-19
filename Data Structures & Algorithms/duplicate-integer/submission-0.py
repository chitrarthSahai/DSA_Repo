class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1
        
        res = [v for v in hashmap.values() if v > 1]

        return True if res else False