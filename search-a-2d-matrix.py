# https://leetcode.com/problems/search-a-2d-matrix

class Solution(object):
    def searchMatrix(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top += 1
            elif target < matrix[mid][0]:
                bot -= 1
            else:
                break
        row = (top + bot) // 2
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[row][mid]:
                return True
            if target > matrix[row][mid]:
                l = l + 1
            else:
                r = r - 1
        return False
        