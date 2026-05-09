class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i : int = 0
        consecutive_count : int = 0
        counter : int = 0
        while i < len(nums):
          
            if nums[i] != 0:
                counter+=1
                consecutive_count = max(consecutive_count,counter)
                i+=1
            else:
                counter = 0
                i+=1
        return consecutive_count

