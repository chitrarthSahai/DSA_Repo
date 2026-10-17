class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Suffix max approach

        # We traverse right to left and maintain a rightMax i.e. a maximum seen from the right side. When we reach i, the current rightMax is the highest element to the right of i, so we can update arr[i] to right Max. But we also account for arr[i] to update the rightMax as well, because arr[i] could be a rightMax for arr[i-1].
        n = len(arr)
        # Create a result array
        res = [0] * n

        # rightMax to -1
        rightMax = -1

        #inversely traverse from n-1, to 0
        for i in range(n - 1, -1, -1):
            #Set result array to current rightMax
            res[i] = rightMax
            #update rightMax
            rightMax = max(rightMax, arr[i])

        return res
