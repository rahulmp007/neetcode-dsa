class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matched_substring = []
        i : int = 0

        while i < len(words):
            j : int = 0
            while j < len(words):
                if i != j and words[j] in words[i]:
                    if words[j] not in matched_substring:
                        matched_substring.append(words[j])
                j+=1
            i+=1
        return matched_substring    