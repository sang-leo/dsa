class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set()
        for i, n in enumerate(nums):
            if n in numset:
                return True
            else:
                numset.add(n)
        return False
        