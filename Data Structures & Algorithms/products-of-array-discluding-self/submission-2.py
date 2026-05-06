class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ne = len(nums)
        left = [1] * ne
        right = [1] * ne
        res = [1] * ne
        left[0] = 1
        right[ne-1] = 1
        for i in range(1, ne):
            left[i] = nums[i-1] * left[i-1]
        for i in range(ne-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
        for i in range(ne):
            res[i] = left[i] * right[i]
        return res
