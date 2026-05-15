class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        substitutes = {}
        used_chars = set()

        for i in range(len(s)):

            if s[i] in substitutes:
                if substitutes[s[i]] != t[i]:
                    return False
            
            else:

                if t[i] in used_chars:
                    return False

                substitutes[s[i]] = t[i]
                used_chars.add(t[i])
        return True