# Input:    a string (s)
# Task:     determine minimum number of partitions possible
# Output:   return integer (min number of partitions)

# Iterate through the string, using a set to hold characters in the current
# partition. If a char is already in the set, increment count that was initialized
# to 1, clear set, then add the char to it. Return count. Time complexity is O(n)
# to traverse the string. Membership checks in an unordered set are done in
# constant time. Space complexity is O(n) if every letter is unique.

class Solution:
    def partitionString(self, s: str) -> int:
        p = set()
        count = 1

        for c in s:
            if c in p:
                count += 1
                p.clear()
                p.add(c)
            else:
                p.add(c)
        
        return count