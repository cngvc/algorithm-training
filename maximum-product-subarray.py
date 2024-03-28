# https://leetcode.com/problems/maximum-product-subarray

class Solution(object):
    def maxProduct(self, nums):
        res = max(nums)
        curMax, curMin = 1, 1
        for n in nums:
            if n == 0:
                curMax = 1
                curMin = 1
                continue
            tmp = n * curMax
            curMax = max(tmp, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res