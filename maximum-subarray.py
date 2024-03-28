# https://leetcode.com/problems/maximum-subarray

import sys

class Solution(object):
    def maxSubArray(self, nums):
        maxS = -sys.maxint
        curS = 0
        for n in nums:
            if curS < 0:
                curS = 0
            curS += n
            maxS = max(curS, maxS)
        return maxS
        