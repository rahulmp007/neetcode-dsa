class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_map = {}
        count = 0
        items = []
        for num in nums:
            if num not in frequent_map:
                frequent_map[num] = count+1
            else:
                frequent_map[num] = frequent_map[num] + 1
        return list(sorted(frequent_map,key=frequent_map.get,reverse=True))[:k]   