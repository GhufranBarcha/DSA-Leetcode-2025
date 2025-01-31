class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = 0
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if s[i+1] == s[j]:
                    count += 1
                    i += 1
                elif s[i] == s[j-1]:
                    count += 1
                    j -= 1
                else:
                    return False
            if count > 1:
                return False
        
        return True                 

        # temp = s
        # if temp[:-1] == temp[:-1][::-1]:
        #     return True        
        # i = 0
        # while i < len(s):
            
        #     if temp == temp[::-1]:
        #         return True

        #     temp = s[:i] + s[i+1:]    
        #     i += 1

        # return False        

        