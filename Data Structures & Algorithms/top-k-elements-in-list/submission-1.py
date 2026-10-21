class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Simple implementation - Pythonic

        return list(map(lambda x: x[0], Counter(nums).most_common(k)))