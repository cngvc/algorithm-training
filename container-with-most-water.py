# https://leetcode.com/problems/container-with-most-water

# Error: out of memory
# class Solution(object):
#     def maxArea(self, height):
#         res = 0
#         for l in range(len(height) - 1):
#             for r in range(l + 1, len(height)):
#                 res = max(res, (r - l) * min(height[l], height[r]))
#         return res

class Solution(object):
    def maxArea(self, height):
        l, r, res = 0, len(height) - 1, 0
        while l < r:
            res = max(res, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res