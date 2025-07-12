class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_chars = {}
        for char in s:
            if char in s_chars:
                s_chars[char] += 1
            else:
                s_chars[char] = 1
        for letters in t:
            if letters in s_chars:
                s_chars[letters] -= 1
            else: 
                return False
            if s_chars[letters] < 0:
                return False
        return True
