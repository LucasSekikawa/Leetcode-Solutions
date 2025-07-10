class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        end = len(nums) - 1
        beginning = 0
        while end >= beginning:
            middle = (beginning + end) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                end = middle - 1
            else:
                beginning = middle + 1
        return beginning
