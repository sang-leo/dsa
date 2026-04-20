class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            sortword = "".join(sorted(word))
            if sortword not in hashmap:
                hashmap[sortword] = [word]
            else:
                hashmap[sortword].append(word)
        return list(hashmap.values())  