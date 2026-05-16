class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i: int = 0
        planted: int = 0

        while i < len(flowerbed):
            if flowerbed[i] != 0:
                i += 1
            else:
                left_empty = i == 0 or flowerbed[i - 1] == 0
                right_empty = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    planted += 1
                
            i+=1
        return planted >= n