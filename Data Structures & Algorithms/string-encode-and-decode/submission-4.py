class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
        # Format: length + delimiter + string
            res += f"{len(s)}#{s}"
        return res   

    def decode(self, s: str) -> List[str]:
        strs : list = []
        i : int = 0

        while i < len(s):
            num : str = ""
            while s[i] != '#':
                num = num + s[i]
                i+=1
            
            word_len = int(num)
            i = i+1

            secret_word = s[i : i+word_len]
            strs.append(secret_word)
            i+=word_len
        
        return strs


