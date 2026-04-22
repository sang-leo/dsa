class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
        res = hashmap.items()
        sortres = sorted(res, key= lambda x:x[1], reverse=True)
        result = []
        for key, value in sortres[:k]:
            result.append(key)
        return result

        