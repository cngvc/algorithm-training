# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Error: out of memory
# class Solution(object):
#     def maxProfit(self, prices):
#         r = 0
#         for i in range(len(prices) - 1):
#             for j in range(i + 1, len(prices)):
#                 r = max(prices[j] - prices[i], r)
#         return r

class Solution(object):
    def maxProfit(self, prices):
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                maxP = max(prices[r] - prices[l], maxP)
            else:
                l = r
            r += 1
        return maxP