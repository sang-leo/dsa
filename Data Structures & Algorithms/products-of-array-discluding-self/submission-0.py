class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodarr = [1] * len(nums)
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    prod *= nums[j]
            prodarr[i] = prod
        return prodarr


        