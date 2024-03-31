# https://leetcode.com/problems/number-of-1-bits

class Solution(object):
    def hammingWeight(self, n):
        res = 0
        while n > 0:
            temp = n % 2
            if temp == 1:
                res += 1
            n = n // 2
        return res
        