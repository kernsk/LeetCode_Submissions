from collections import deque

class Solution:
    # Input: two strings
    # Task: combine them alternatingly, beginning with word1; append excess
    # Output: one string

    # First working attempt
    # def mergeAlternately(self, word1: str, word2: str) -> str:
        # idx1, idx2 = 0, 0
        # str_builder = []
        # switch = True

        # while idx1 < len(word1) and idx2 < len(word2):
        #     if switch:
        #         str_builder.append(word1[idx1])
        #         idx1 += 1
        #     else:
        #         str_builder.append(word2[idx2])
        #         idx2 += 1
        #     switch = not switch
        
        # result = "".join(str_builder)
        # result += word1[idx1::] if idx1 < len(word1) else word2[idx2::]
        # return result 

    def mergeAlternately(self, word1: str, word2: str) -> str:
        q1 = deque(word1)
        q2 = deque(word2)
        sb = []

        while q1 or q2:
            if q1:
                sb.append(q1.popleft())
            if q2:
                sb.append(q2.popleft())

        return ''.join(sb)