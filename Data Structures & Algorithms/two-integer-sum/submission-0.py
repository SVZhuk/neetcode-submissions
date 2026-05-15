class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = None, None
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


Solution1 = Solution()
Solution1.twoSum([3, 4, 5, 6], 7)