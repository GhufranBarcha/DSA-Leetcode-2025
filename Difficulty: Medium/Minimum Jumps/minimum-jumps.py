class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # Edge cases
        if n == 1:
            return 0  # Already at the end
        if arr[0] == 0:
            return -1  # Can't move from the first position
        
        max_reach = arr[0]  # Maximum reachable index so far
        current_end = arr[0]  # End of the current jump range
        jumps = 1  # At least one jump is needed

        for i in range(1, n):
            # Check if we've reached the last index
            if i == n - 1:
                return jumps
            
            # Update the maximum reach
            max_reach = max(max_reach, i + arr[i])
            
            # If we reach the end of the current jump
            if i == current_end:
                jumps += 1
                current_end = max_reach  # Move to the next range
                
                # If the current end cannot move forward, return -1
                if current_end <= i:
                    return -1
        
        return -1  # If we exit the loop without reaching the end



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends