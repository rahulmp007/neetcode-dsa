class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_so_far = -1
            for j in range(i+1,len(arr)):
                if arr[j]> max_so_far:
                    max_so_far = arr[j]
            arr[i] = max_so_far
        return arr