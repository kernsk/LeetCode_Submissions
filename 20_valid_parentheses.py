# Input:    a string
# Task:     determine if the string, containing different types of brackets, is valid
# Valid:    open brackets must be closed by the same type of brackets
#           open brackets must be closed in the correct order
#           every close bracket has a corresponding open bracket of the same type
# Output: a boolean

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        front = {')': '(', '}': '{', ']': '['}
        opened = []

        for b in s:
            if b in front.values():
                opened.append(b)
            elif b in front:
                if not opened or opened[-1] != front[b]:
                    return False
                opened.pop()
        return not opened