# https://leetcode.com/problems/counting-bits

class Solution(object):
    def countBits(self, n):
        dp = [0] * (n + 1)
        offsets = 1
        for i in range(1, n + 1):
            if offsets * 2 == i:
                offsets = i
            dp[i] = 1 + dp[i - offsets]
        return dp