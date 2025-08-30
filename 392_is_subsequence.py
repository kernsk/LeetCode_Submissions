# Input:    two strings
# Task:     determine if the first is a subsequence of the second; must appear in the same order
# Output:   a boolean

# The brute force approach would be to iterate through s, then t in a nested loop
# starting one index past where the last character of s was found. You could create
# an array the length of s, initialized to 0, to hold the index where each char was
# found. If a char isn't found, you return false. If you make it through the nested
# loops, return true. This may be the most optimal in time complexity because the
# two strings are ordered for all intents and purposes. We have to maintain order.
# The time complexity simplifies to O(n) where n is s because we aren't starting over at the
# beginning of string t for every iteration. The space complexity is O(n) because we create
# the array to hold the indices of each char we find.

# An improvement would be to use a two pointer style approach. It has the same time complexity,
# but doesn't require additional space beyond the two pointers. It is also much less code.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)