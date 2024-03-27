# https://leetcode.com/problems/coin-change/
# solution includes the concepts of dynamic programming

import sys

class Solution(object):
    def coinChange(self, coins, amount):
        db = [sys.maxint] * (amount + 1)
        db[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    db[i] = min(db[i], 1 + db[i - c])
        return db[amount] if db[amount] < sys.maxint else -1