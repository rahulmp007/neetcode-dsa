class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group : dict = {}

        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))

            if key not in anagram_group:
                anagram_group[key] = [strs[i]]
            else:
                values : list = anagram_group[key]
                values.append(strs[i])

        return list(anagram_group.values())
        