class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i : int = 0
        j : int = 0
        while j < len(nums):
            if nums[j] == val:
                j+=1
            else:
                [nums[i],nums[j]] = [nums[j],nums[i]]
                i+=1
                j+=1
        return len(nums[:i])
           
        
        