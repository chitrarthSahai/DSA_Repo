class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #My approach-
        #Whenever we see a frequency question, our intuition would be to use a hashmap to maintain count.
        # The ideal hashmap for this is a defaultdict(int) because integer values can maintain counts of occurences.

        #To maintain count
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1

        return list(dict(sorted(hashmap.items(), key= lambda item: item[1], reverse=True)).keys())[:k]

        