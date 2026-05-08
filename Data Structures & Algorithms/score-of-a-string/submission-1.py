class Solution:
    def scoreOfString(self, s: str) -> int:
        score:int = 0

        i : int = 0
        j : int = 0


        while (i < len(s)-1):
            j+=1
            high = ord(s[j])
            low = ord(s[i])
            i+=1

            score = score + abs(high - low)
        return score
        