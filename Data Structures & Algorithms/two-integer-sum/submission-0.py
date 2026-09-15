class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(0, len(nums)):
            if (target - nums[i]) in seen:
                return [seen[target-nums[i]], i]

            else:
                seen[nums[i]] = i
