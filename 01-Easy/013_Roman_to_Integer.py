class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        sum_values = 0
        i = len(s)-1
        while i >= 0:
            if i == 0:
                current_value = values[s[i]]
            else:
                if values[s[i-1]] < values[s[i]]:
                    current_value = values[s[i]] - values[s[i-1]]
                    i = i - 1
                else:
                    current_value = values[s[i]]
            sum_values += current_value
            i = i - 1
        return sum_values
