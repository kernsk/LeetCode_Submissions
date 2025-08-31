# Input:    an integer array and an integer
# Task:     find a contigous subarray whose length is equal to the given integer that has
#           the maximum average value 
# Output:   an float

# The brute force method would be to iterate through nums and at each step add up nums[i] through nums[i + 3],
# then return that value. It has a simplified time complexity of O(n * k) and space complexity of O(1).

# The brute force method has a lot of overlapping subproblems, so an improvement would be to use the sliding
# window method. We'll sum the initial k number of values. When we slide to the right, we only need to subtract
# the previous left value and add the new right value. Lastly, we return the max_sum divided by k.
# This will give us a time complexity of O(n), while maintaining constant space complexity.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        max_sum = curr
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            if max_sum < curr:
                max_sum = curr
        return max_sum/k