# Input:    array of integers
# Task:     determine if number of occurences of each value is unique
# Output:   boolean

# A brute force approach would be to use a nested loop. For each value, search the
# rest of the array and count how many times it occurs. You could use a second
# array to hold the values that have already been counted to make sure you don't
# count them more than once. This is quite inefficient as the time complexity can
# reach O(n^3) if the values are all different. The space complexity would be O(n)
# for the two extra arrays.

# You could improve this by using a greedy approach and sorting the array, but
# the most efficient way would be to use a dictionary to store the values with
# their respective counts. You can traverse the list of values from the dictionary
# and push the counts into a set, one by one, if they aren't already in the set.
# If they are, return false. If you get through the whole loop, return true. Time
# complexity is O(n). Space complexity is O(n).

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = dict()
        uniq_vals = set()

        for num in arr:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        vals = counts.values()

        for val in vals:
            if val not in uniq_vals:
                uniq_vals.add(val)
            else:
                return False
        return True