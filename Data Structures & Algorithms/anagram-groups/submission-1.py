class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            word = "".join(sorted(s))
            if word not in hashmap:
                hashmap[word] = [s]
            else:
                hashmap[word].append(s)
        return list(hashmap.values())