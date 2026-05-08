class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splits = s.split()
        return len(splits[len(splits)-1])