# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_value = 0
        length = len(s)
        i,j = 0, 0
        set_ = set()
        while i < length and j < length:
            if s[j] not in set_:
                set_.add(s[j])
                if j+1-i > max_value:
                    max_value = j+1-i
                j += 1
            else:
                set_.remove(s[i])
                i += 1
        return max_value