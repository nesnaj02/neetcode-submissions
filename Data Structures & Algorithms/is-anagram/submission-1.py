class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        newlists = sorted(s)
        newlistt = sorted(t)
        for i in range(len(newlists)):
            if newlists[i] != newlistt[i]:
                return False
            
        return True