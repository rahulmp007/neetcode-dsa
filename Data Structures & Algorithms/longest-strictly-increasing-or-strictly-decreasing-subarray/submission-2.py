class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_length = 1
        n = len(nums)
        for i in range(n):
            increasing = 1
            decreasing = 1
            for j in range(i + 1, n):
                if nums[j] > nums[j - 1]:
                    increasing += 1
                else:
                    increasing = 1

                if nums[j] < nums[j - 1]:
                    decreasing += 1
                else:
                    decreasing = 1

                max_length = max(max_length, increasing, decreasing)

        return max_length
        