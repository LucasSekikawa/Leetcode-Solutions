class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_global = nums[0]
        for i in range(1, len(nums)):
            current_num = nums[i]
            current_sum = max(current_num, current_sum + current_num)
            max_global = max(max_global, current_sum)
        return max_global
