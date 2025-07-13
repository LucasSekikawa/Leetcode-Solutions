class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        result_sum = []
        carry = 0
        while (i >= 0) or (j >= 0) or (carry > 0) :
            if i >= 0:
                current_a_bit = int(a[i])
            else:
                current_a_bit = 0
            if j >= 0:
                current_b_bit = int(b[j])
            else:
                current_b_bit = 0
            sum = current_a_bit + current_b_bit + carry
            result_bit = sum % 2
            carry = sum // 2
            result_sum.append(str(result_bit))
            i -= 1
            j -= 1
        result_sum.reverse()
        return ("".join(result_sum))
