class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # As both arrays are sorted and can be simply merged, we can try to fit this in the merge sort logic, specifically the merge function of the mergeSort. The only thing is we need to overwrite nums1, but we risk overwriting the values we need for further analysis. For this we can start with a copy of nums1 and use that as nums1, while nums1 can be safely overwritten with new values

        nums1_copy = nums1[:m] #copy only valid m elements

        #three pointers, one of copy, one for nums2, and a write pointer over nums1
        idx = i = j = 0

        while idx < m + n:

            # note this condition, if j is equal to or greater than n, that means nums2 has been already traversed, and j is out of bounds, so the remaining thing is to copy over the nums1_copy elements to nums1, so we use or here. With this we also avoid an elif because for the else condition runs only if j is in bound and nums2[j] is less than nums1_copy
            if j>=n or (i < m and nums1_copy[i] <= nums2[j]):
                nums1[idx] = nums1_copy[i]
                i += 1
            else:
                nums1[idx] = nums2[j]
                j += 1
            idx += 1

