class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        hashmap = {}
        l = len(nums)
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
            if hashmap[n] > l//3 and n not in res:
                    res.append(n)
        return res
        