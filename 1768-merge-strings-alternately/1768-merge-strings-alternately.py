class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len1 = len(word1)-1
        len2 = len(word2)-1

        total = ""
        i = 0
        while i <= max(len1 , len2 ):

            if i <= len1:
                total += word1[i]
            if i <= len2:
                total += word2[i]
            i += 1
        return total
