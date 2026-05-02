class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_look_up = set(nums)
        streak : int = 0
        for i in range(len(nums)):

            if nums[i] - 1 not in nums_look_up:
                
                consecutive_sequence_counter = 0
                anchor_ele = nums[i]
                
                while anchor_ele in nums_look_up:
                    consecutive_sequence_counter+=1
                    anchor_ele+=1
                
                streak = max(streak,consecutive_sequence_counter)
            else:
                i+=1
        return streak



         