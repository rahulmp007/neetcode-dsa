class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            if len(nums) == 0:
                return []
            dict = {}
            for i,num in enumerate(nums):
                diff = target - num
                if diff in dict:
                    return [dict[diff],i]
                else:
                    dict[num] = i
            return []
