class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count : int = 0
        key : int = 0
        for i in range(len(nums)):

            if count == 0:
                key = nums[i]
            
            if key == nums[i]:
                count+=1
            else:
                count-=1
        return key
        
        