class Solution:
    # Input: a string
    # Task: reverse the vowels in the string
    # Output: a string
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        st = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        v = set(vowels)

        while left < right:
            ch1 = st[left].lower()
            ch2 = st[right].lower()
            if ch1 in v and ch2 in v:
                st[left], st[right] = st[right], st[left]
                left += 1
                right -= 1
            elif ch1 in v:
                right -= 1
            elif ch2 in v:
                left += 1
            else:
                left += 1
                right -= 1
        return ''.join(st)