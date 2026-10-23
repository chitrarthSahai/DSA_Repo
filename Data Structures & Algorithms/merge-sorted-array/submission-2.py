class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # The most brute idea is nums1 have garbage values that can be replaced by nums2, nums1 is always m+n, where m is valid values in nums1 and n is size of nums2. We can simply replace the values after m with nums2

        nums1[m:] = nums2[:n]

        #sort nums1 in place
        nums1.sort()

        #Time complexity - O((m+n)log(m+n)), because of the sorting in place using standard library
        #Space complexity - O(m+n) or O(1) again due to sorting in place
        
        #next solution will be better