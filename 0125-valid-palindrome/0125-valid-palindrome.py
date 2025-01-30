class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        str1 = ""
        for i in s:
            if i.isalnum():
                str1 += i

        start = 0
        end = len(str1) - 1
        while start < end:
            if str1[start] != str1[end]:
                return False
            start += 1
            end -= 1
        return True


        