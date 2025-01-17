class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        arr = []
        for i in s:
            if i.isalnum():
                arr.append(i)

        char = "".join(arr)        
        if char == char[::-1]:
            return True
        return False    