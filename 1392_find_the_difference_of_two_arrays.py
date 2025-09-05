# Input:        two 0-indexed integer arrays of equal length
# Task:         • create two lists of distinct integers
#               • each list indicates the membership of integers found in one of
#                 the given arrays, but not the other
#               • Order of ints is irrelevant
# Output:       a list containing the two created lists
# Constraints:  list length is between 1 and 1000
#               integers range from -1000 to 1000

# The brute force approach, you would create two lists – one for each of the non-membership
# lists. For each integer of one list, you would compare it against each integer of the
# other list. If it's not found, you add it to list1. You do the same thing in reverse
# to gather the integers only in the second list. Append each to the result and return it.
# The simplified time complexity is O(n^2). The simplified space complexity is O(n). One thing
# to note is that you would have to add logic to account for duplicates.

# An improvement over that approach would be to create a set of each of the two given lists to
# remove all dupes. Iterate over the first set (s1), checking for membership in the second set (s2)
# in constant time. Integers not in s2 are added to a new list (list1). Repeat by iterating over
# s2 and appending results to a second list (list2). Return the combined lists. The simplified time
# complexity is O(n) and the simplified space complexity is O(n). This cuts the time complexity
# because hash sets can do membership checks in constant time.  Hash sets also do not allow duplicates,
# ensuring each distinct integer is only checked against the other set once.

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        list1 = []
        list2 = []

        for num in s1:
            if num not in s2:
                list1.append(num)

        for num in s2:
            if num not in s1:
                list2.append(num)
        
        return [list1, list2]