class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numbers = {}
        for i in range(0, len(nums)):
            current_num = nums[i]
            if current_num in numbers:
                if (abs(numbers[current_num]-i)) <= k:
                    return True
                else:
                    numbers[current_num] = i
            else:
                numbers[current_num] = i
        return False
