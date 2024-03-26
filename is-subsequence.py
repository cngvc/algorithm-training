# https://leetcode.com/problems/is-subsequence/

class Solution(object):
    def isSubsequence(self, s, t):
        s_idx = 0
        t_idx = 0
        if len(s) == 0: return True
        while s_idx < len(s) and t_idx < len(t):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            t_idx += 1
        return s_idx == len(s)
        