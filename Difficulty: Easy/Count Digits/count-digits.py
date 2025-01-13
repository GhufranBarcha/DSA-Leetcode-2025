#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        # code here
        
        count = 0
        m = n
        
        while m > 0:
            
            digit = m % 10
            
            if digit != 0 and n % digit ==0:
                count += 1
                
            m = m // 10
            
        return count    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.evenlyDivides(N))
        print("~")

# } Driver Code Ends