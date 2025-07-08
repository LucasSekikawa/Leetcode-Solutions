class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        new_string = s.rstrip().lstrip().replace(" ", "-")
        list_string = list(new_string)
        count = 0
        for i in range(len(list_string)-1, -1, -1 ):
            if list_string[i] != "-":
                count += 1
            else:
                break
        return count
