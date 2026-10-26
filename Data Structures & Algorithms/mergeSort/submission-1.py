# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        # Now let's implement the mergeSort Solution for this.

        #implement the merge sort function

        def mSort(lst, start, end):
            if end - start + 1 <= 1:
                return lst

            mid = (end + start) // 2 #Calculate mid

            #Recurisively call mSort to break this down into sublist till above if condition satisfy and the recursion loop starts soaring from the depth.

            mSort(lst, start, mid)
            mSort(lst, mid+ 1, end)

            #Call the merge function, implemented later.
            merge(lst, start, mid, end)


        #The merge function
        def merge(arr, s, m, e):

            #Slice the left and right half from the input list

            L = arr[s:m+1]
            R = arr[m+1:e+1]

            i = j = 0 #pointers for left and right half
            k = s #write pointer for arr, this is set to start because the merge of L and R has to written to the start index of the arr in the current recursion depth. Let's say the last 2 index of input list was sliced to 2 sublists of 1 element in mSort call, so when this merge is called, the output should be written to n-2 and n-1 index, which in this case would be the start index of mSort in that call.

            while i < len(L) and j < len(R):
                if L[i].key <= R[j].key:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                
                k += 1

            #The above loop ends, when one of the slice ends early, so for the remaining elements in the other slice, we need to simply merge them as it is.

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

        #The main call to mSort
        mSort(pairs, 0, len(pairs)-1)

        return pairs
            

