class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = -1
        for i in range(len(arr) - 1 , -1 , -1):
            
            cur_max = arr[i]
            arr[i] = maxi
            maxi = max (cur_max , maxi)
            
        return arr 

             
        