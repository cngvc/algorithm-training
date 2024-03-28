# https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        res = [0] * len(nums)
        prefix = 1
        for i in range(len(res)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(res) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
