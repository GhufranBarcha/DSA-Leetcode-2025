class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen= float('inf')
        strs.sort()

        for l in strs:
            minlen = min(len(l), minlen)

        if minlen == 0:
            return ""
        for n in range(minlen):
            val = True
            for i in range(len(strs) - 1):
                if strs[i][:n] != strs[i + 1][:n]:
                    if n == 0:
                        return "" 
                    return strs[i][:n-1]
        return strs[0]              
        