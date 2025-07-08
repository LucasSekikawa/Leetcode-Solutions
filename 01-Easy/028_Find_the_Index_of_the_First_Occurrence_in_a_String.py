class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        else:
            for i in range(0, len(haystack)-len(needle)+1 ):
                count = 0
                j = 0
                if (haystack[i] == needle[j]):
                    count = 1
                    for j in range(1, len(needle)):
                        if (haystack[i+j] != needle[j]):
                            break
                        else:
                            count += 1
                if count == len(needle):
                    return i
            return -1
