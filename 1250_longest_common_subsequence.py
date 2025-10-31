# Input:    two strings
# Task:     determine longest common subsequence
# Output:   integer

# The most efficient approach would be to use a tabular dynamic
# programming approach. The time complexity would be O(n * m). We
# could reduce the space complexity from O(n * m) down to O(n) by
# only keeping track of the necessary row above.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = (n + 1) * [0]

        for i in range(0, m):
            prev = 0
            longest = 0
            for j in range(1, n + 1):
                if text2[j - 1] == text1[i]:
                    longest = 1 + prev
                else:
                    longest = max(dp[j - 1], dp[j], prev)
                prev = dp[j]
                dp[j] = longest

        return dp[n]