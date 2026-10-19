class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # A more efficient logic, same as previous

        seen = {}

        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                return True
            
        return False