class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #Brute force
        n = len(arr)

        for i in range(n):
            max_num = -1

            if i == n-1:
                arr[i] = -1
                break
            
            for j in range(i+1, n):
                max_num =  max(max_num, arr[j])
            
            arr[i] = max_num
        
        return arr