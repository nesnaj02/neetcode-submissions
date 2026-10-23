class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)): #go through each word after the first
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]: #find first letter mismatch
                    break
                j += 1
            prefix = prefix [:j]
        return prefix
                



