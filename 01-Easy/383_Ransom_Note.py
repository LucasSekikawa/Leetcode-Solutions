class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letters = {}
        for char in magazine:
            if char in magazine_letters:
                magazine_letters[char] += 1
            else:
                magazine_letters[char] = 1
        for letters in ransomNote:
            if letters in magazine_letters:
                magazine_letters[letters] -= 1
            else:
                return False
            if magazine_letters[letters] < 0:
                return False
        return True
