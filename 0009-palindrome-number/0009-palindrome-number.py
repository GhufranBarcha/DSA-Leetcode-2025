class Solution:
    def isPalindrome(self, x: int) -> bool:
        ## Brute force
    #    return True if  str(x)[::-1] == str(x) else False

        ## Efficient way

        if x < 0:
            return False
        reverse = 0
        xcopy = x

        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x = x // 10

        return reverse == xcopy    
        
       


