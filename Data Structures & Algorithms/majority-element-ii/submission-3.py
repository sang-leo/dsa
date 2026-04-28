class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        hashmap = {}
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
            if hashmap[n] > len(nums)/3 and n not in res:
                    res.append(n)
        return res

