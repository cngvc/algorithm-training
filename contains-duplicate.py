# https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        hs = set()
        for n in nums:
            if n in hs:
                return True
            hs.add(n)
        return False