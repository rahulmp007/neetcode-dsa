class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            groups = {}
            for word in strs:
                word_srorted = "".join(sorted(word))
                if word_srorted in groups:
                    current_values = groups[word_srorted] 
                    current_values.append(word)
                else:
                    groups[word_srorted] = [word]

            return list(groups.values()) 
        