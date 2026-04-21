class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        count = len(nums)/2
        for i, n in enumerate(nums):
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
            if hashmap[n] >= count:
                return n
        
        