#User function Template for python3

class Solution:
    def sumOfSeries(self,n):
        #code here
        all_sum = 0
        for d in range(1, n+1):
            all_sum += d**3
            
        return all_sum    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sumOfSeries(N)) 
        print("~")
# } Driver Code Ends