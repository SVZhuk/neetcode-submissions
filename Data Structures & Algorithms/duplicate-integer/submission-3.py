class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        collection = set()
        for i in nums:
            if i in collection:
                return True
            else:
                collection.add(i)
        return False
         