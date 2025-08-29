# Input:    a list of integers and a singular integer
# Task:     find the two indices whose values add up to the singular integer (target)
# Output:   a list containing the two indices (order doesn't matter)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stash = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in stash:
                return [stash[diff], i]
            stash[num] = i
        return None