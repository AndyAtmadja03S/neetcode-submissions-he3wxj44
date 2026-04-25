class Solution:
    def numDecodings(self, s: str) -> int:

        ways = [0] * (len(s) + 1)
        ways[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            ways[i] = 0

            # take 1 digit
            if s[i] != '0':
                ways[i] += ways[i+1]

            # take 2 digits
            if 10 <= int(s[i:i+2]) <= 26:
                ways[i] += ways[i+2]
        return ways[0]