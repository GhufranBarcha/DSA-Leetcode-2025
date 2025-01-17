#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List
import math


# } Driver Code Ends

#User function Template for python3

class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        a1 ,b1 = a, b
        while b != 0:
            a , b = b , a % b
            
        lcm = (a1 * b1)/a
        
        return [int(lcm), a]

#{ 
 # Driver Code Starts.


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        a = int(input())
        b = int(input())
        obj = Solution()
        res = obj.lcmAndGcd(a, b)
        print(f"{res[0]} {res[1]}")
        print("~")

# } Driver Code Ends