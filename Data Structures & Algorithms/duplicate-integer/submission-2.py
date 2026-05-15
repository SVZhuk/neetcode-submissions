class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        col = {}
        for i in nums:
            if i in col.keys():
                return True
            else:
                col[i] = 1
        return False