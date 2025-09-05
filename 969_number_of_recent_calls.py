# Input:        an integer representing time in milliseconds
# Task:         determine how many requests have been made in the past 3000 millseconds
# Output:       an integer
# Constraints:  time (t) won't be lower than 1
#               t values will be strictly increasing

# The brute force approach would be to collect every ping into a list (recent), then
# when ping is called you append the value t to the end of the list and iterate through
# the entire list counting every value that is greater than or equal to t - 3000. Return
# that value. The time complexity of an individual ping is O(n) where n is the size of
# the ping list. The space complexity is also O(n). For both, keep in mind that n grows
# with each ping. If you consider the program as a whole and factor in the number of pings (m),
# then the time complexity would be O(n*m).

# An improvement would be to use a queue because you can pop elements from the front in
# constant time that are less than t - 3000. This will keep n as small as possible (capping
# it at a size of 3000). Iterate through the queue popping elements until you reach one within
# 3000 of t, then exit and return the size of the queue as your answer.  The time complexity
# and space complexity are O(1) because the queue is bounded to a max size of 3001 in the worst
# case. If you consider the program as a whole and factor in the number of pings (m), then the
# time complexity would be O(m).

from collections import deque

class RecentCounter:
    def __init__(self):
        self.recent = deque()
        
    def ping(self, t: int) -> int:
        self.recent.append(t)
        while (self.recent[0] < (t - 3000)):
            self.recent.popleft()
        return len(self.recent)


#-------- LeetCode's own added notes -----------------------------

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)