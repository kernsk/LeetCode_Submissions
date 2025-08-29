class Solution:

    # Input: two strings
    # Output: one string; the greatest common devisor
    # Approach: Test if a GCD exists. If not, return an empty string. Next, we calculate how large the GCD is. To do
    #           that, we need to figure out which string is smaller and iterate over that range of integers in reverse
    #           order until we find one that both string lengths are divisible by. We capture the substring up to that value,
    #           calculate how many times it fits into the length of the longer string, then create a new string that is just
    #           the GCD we're testing multiplied to match the length of the longest.  We compare them – if it's a match, we
    #           return that GCD.  If we iterate through the range of ints and don't find a GCD, we return an empty string.

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == 1:
            return str1
        if len(str2) == 1:
            return str2

        sz1 = len(str1)
        sz2 = len(str2)
        length = min(sz1, sz2)
        longer = str1 if sz1 > sz2 else str2

        for i in range(length, 1, -1):
            if sz1 % i == 0 and sz2 % i == 0:
                base = str1[:i]
                mult = len(longer) // i
                if longer == (base * mult):
                    return base
        return ""

# Alternatively, the built-in method also works, but I wanted to work through it without it.
    # def gcdOfStrings(self, str1: str, str2: str) -> str:
    #     if str1 + str2 != str2 + str1:
    #         return ""
    #
    #     gcd_length = gcd(len(str1), len(str2))
    #     return str1[:gcd_length]