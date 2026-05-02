class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct_items = {}
        for num in nums:
            if num in distinct_items:
                return True
            distinct_items[num] = str(num)
        return False