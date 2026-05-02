class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_array = [None]*len(nums)
        for i, item in enumerate(nums):
            result : int = 1
            for j,item in enumerate(nums):
                if i != j:
                    result = result * nums[j]
        
            result_array[i] = result
        
        return result_array