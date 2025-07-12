class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        char_to_word = {}
        word_to_char = {}

        for i in range(len(pattern)):
            char_p = pattern[i]
            word_s = words[i]
            if char_p in char_to_word:
                if char_to_word[char_p] != word_s:
                    return False  
            else:
                char_to_word[char_p] = word_s
            if word_s in word_to_char:
                if word_to_char[word_s] != char_p:
                    return False 
            else:
                word_to_char[word_s] = char_p
        return True
