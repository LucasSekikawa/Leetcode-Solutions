class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        count = 0
        j = 0
        for i in range(0, len(t)):
            if t[i] == s[j]:
                j += 1
                count += 1
            if count == len(s):
                return True
        return False
