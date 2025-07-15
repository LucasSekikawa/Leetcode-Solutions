# First solution i got
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        numbers = {}
        for i in range(0, len(nums)):
            current_num = nums[i]
            if current_num not in numbers:
                numbers[current_num] = 1
            else:
                numbers[current_num] += 1
                if numbers[current_num] > (len(nums) / 2):
                    return current_num

# Second one 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
