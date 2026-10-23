class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #The clean approach and most optmized, without using extra space. Reverse our approach, instead of finding the smaller of the two arrays and writing them in the beginning of the array, we can start the write pointer on nums1 from the end of the array and overwrite garbage values by comparing the larger of nums1 valid elements and nums2, however the comparison pointer for nums1 starts from the last valid element m - 1 and for nums2 it is n - 1 (it's last element). To optmize this we need to realize that once nums2 fits inside nums1, the problem is solved, so no need to care for nums1 pointer going to 0.

        #the writer initializes at the end index of nums1
        last = m + n - 1

        #The i is nums1 pointer for valid elements, j is nums2 pointer (all are valid in nums2)
        i, j = m - 1, n - 1

        #only loop till nums2 is traversed completely
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1

            last -= 1

        