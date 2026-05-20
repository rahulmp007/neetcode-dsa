class Solution:
    def maxDifference(self, s: str) -> int:
        char_frequency = {}

        for i in range(len(s)):
            if s[i] in char_frequency:
                char_frequency[s[i]] = char_frequency.get(s[i],0) + 1
            else:
                char_frequency[s[i]] = 1
        

        frequency_values = char_frequency.values();

        odd_values = [x for x in frequency_values if x % 2 != 0]
        even_values = [x for x in frequency_values if x % 2 == 0]


        return max(odd_values) - min(even_values)