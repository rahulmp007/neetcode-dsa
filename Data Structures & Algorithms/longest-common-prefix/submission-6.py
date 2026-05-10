class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       

        ref = strs[0]

        i: int = 0

        longest_prefix: str = ""

        while i < len(ref):
            current_char = ref[i]
            j: int = 1

            while j < len(strs):
                if i >= len(strs[j]) or current_char != strs[j][i]:
                    return longest_prefix
                j += 1
            longest_prefix += current_char
            i+=1 
        return longest_prefix     