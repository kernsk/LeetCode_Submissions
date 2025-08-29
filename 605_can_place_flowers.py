class Solution:
    # Input: integer list and integer
    # Task: See if you can place n flowers into the list, while maintaining adjacency rule
    # Output: a boolean
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if(flowerbed[0]):
                return False
            return True

        for i, flower in enumerate(flowerbed):
            if not flower:
                if i == 0 and not flowerbed[i + 1]:
                    flowerbed[i] = 1
                    n -= 1
                elif i == len(flowerbed) - 1 and not flowerbed[i - 1]:
                    flowerbed[i] = 1
                    n -= 1
                elif not flowerbed[i - 1] and not flowerbed[i + 1]:
                    flowerbed[i] = 1
                    n -= 1
            if n == 0:
                return True
        return False