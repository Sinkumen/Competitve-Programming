class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i < len(flowerbed)-1:
                    if flowerbed[i+1]==0:
                        count += 1
                        i += 2
                    else:
                        i += 1
                else:
                    count += 1
                    i += 2
            else:
                i+=2
        return count >= n
        