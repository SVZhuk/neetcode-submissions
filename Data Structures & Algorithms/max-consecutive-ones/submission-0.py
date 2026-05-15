class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current_max = 0
        for num in nums:
            if num == 1:
                current_max += 1
            else:
                max_ones = current_max if current_max > max_ones else max_ones
                current_max = 0


        return max(max_ones, current_max)
           
