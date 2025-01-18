class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        #  code here
        
        dict_n = dict()
        
        for i in arr:
            if i in dict_n:
                dict_n[i] += 1
            else:
                dict_n[i] = 1
        for i in range(len(arr)):
            arr[i] = 0 if dict_n.get(i+1) is None else dict_n.get(i+1)
            
        return arr    
            
            




#{ 
 # Driver Code Starts
# Main code to read input and process each test case
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().frequencyCount(arr)  # find the frequencies

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print the result
    else:
        print("[]")  # Print empty list if no valid frequencies

# } Driver Code Ends