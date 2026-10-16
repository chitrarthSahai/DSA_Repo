class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Last approach was somehwat of partition logic. We maintained a write pointer that lags the main iterator num over the list, specifically halting at the index where val was found and needs to be removed. All the non val elements needs be copied over to k as k move aheads. this is a lot of unnessary copy operations, if count of values tobe removed are too low.

        #We will now look ath the most optmized solution of this problem. The approach is that instead of copying all non vals at k and moving k forward. Why not try to copy the val to the end of the array and discard from the array.
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                n -= 1 #reduce size of list, important for the first run so we don't get outofbounds exception
                nums[i] = nums[n] #swap val to be removed with 
            else:
                i += 1 # This is why we used a while loop, we only increment i in the else condition, so that the if block can run again on the swapped value, imagine the last value swapped in the if block was also the val, so we need to check again and only increment i if okay.

        return n #The number of times n was decremented is when val was found, so remaining value of n are the count of all the non-val items.
