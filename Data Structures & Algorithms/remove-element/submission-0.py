class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k is a write pointer denoting the position where val was found and the following non val items needs to be swapped with
        k = 0

        for num in nums:
            # if num is not val, keep swapping with k, it initially can move with num in sync. that means nums[k] = num will be a self swap. However, see if a num is A val, k stays to the index where val was found, while num moves forward. When another num is found != val, it replaces num[k], making the earlier num[k] having the val removed from the list.
            if num != val:
                nums[k] = num
                k += 1

        return k #k also becomes the count non val was found
