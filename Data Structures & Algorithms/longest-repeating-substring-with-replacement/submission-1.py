class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        L = 0
        max_freq = 0
        max_len = 0

        for R in range(len(s)):
            hm[s[R]] = hm.get(s[R], 0) + 1
            max_freq = max(max_freq, hm[s[R]])

            # if replacements needed > k, shrink window
            while (R - L + 1) - max_freq > k:
                hm[s[L]] -= 1
                L += 1

            max_len = max(max_len, R - L + 1)

        return max_len
