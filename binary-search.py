# https://leetcode.com/problems/binary-search

class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            k = int((r + l) / 2)
            if nums[k] == target:
                return k
            if nums[k] < target:
                l = k + 1
            else:
                r = k - 1
        return -1