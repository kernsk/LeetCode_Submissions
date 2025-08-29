# input: candies array and extraCandies integer
# return: boolean array

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = 0
        result = []

        for num in candies:
            mx = max(mx, num)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= mx:
                result.append(True)
            else:
                result.append(False)

        return result