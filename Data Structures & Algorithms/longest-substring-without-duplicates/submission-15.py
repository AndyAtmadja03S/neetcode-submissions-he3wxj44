class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        L = 0
        max_l = 0

        for R in range(len(s)):
            hm[s[R]] = hm.get(s[R], 0) + 1
            
            while hm[s[R]] > 1:
                hm[s[L]] -= 1
                L += 1

            max_l = max(max_l, R - L + 1)

        return max_l
