#User function Template for python3


class Solution:
    def sumOfDivisors(self, n):
        
        ## Brute Force Approch
    #     all_sum = 0	
    # 	for i in range(1, n+1):
    # 	    for j in range(1 , i + 1):
    # 	        if i % j == 0:
    # 	            all_sum += j
    	            
    # 	return all_sum            
    	sum_all = 0
    	for i in range(1, n+1):
    	    sum_all += (i * (n//i))
    	return sum_all    
    	    
    	


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
        print("~")

# } Driver Code Ends