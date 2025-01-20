class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ## First approch
        # s = s.strip().split(" ")
        # return len(s[-1])

        end = len(s) - 1

        while s[end] == " ":
            end -= 1

        start = end

        while start >= 0 and s[start] != " ":
            start -= 1
        print(start ,end)
        return end - start          