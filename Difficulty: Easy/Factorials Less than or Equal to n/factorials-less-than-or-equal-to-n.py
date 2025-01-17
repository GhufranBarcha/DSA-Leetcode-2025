#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
    	#code here 
    	
    	sum = 1
    	arr = []
    	for i in range(1, n + 1):
    	    sum  = sum * i
    	    if sum > n:
    	        break
    	    arr.append(sum)
    	return arr 
    	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends