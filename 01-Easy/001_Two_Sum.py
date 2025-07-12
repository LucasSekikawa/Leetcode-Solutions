class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(0, len(nums)):
            current_num = nums[i]
            if (target-current_num) in numbers:
                return [ numbers[target-current_num], i ]
            else:
                numbers[current_num] = i
