class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            word = "".join(sorted(s))
            if word in hashmap:
                hashmap[word].append(s)
            else:
                hashmap[word] = [s]
        return list(hashmap.values())
        