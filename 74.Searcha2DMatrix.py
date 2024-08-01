"""You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity."""

"""Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_top = 0
        row_bottom = len(matrix) - 1

        while row_top <= row_bottom:
            row_mid = row_top + (row_bottom - row_top) // 2
            row = matrix[row_mid]
            if row[0] > target:
                row_bottom = row_mid - 1
            elif row[-1] < target:
                row_top = row_mid + 1
            else:
                break
        else:
            return False

        row = matrix[row_mid]
        left = 0
        right = len(row) - 1

        while left <= right:
            mid = left + (right - left) // 2
            val = row[mid]
            if val > target:
                right = mid - 1
            elif val < target:
                left = mid + 1
            else:
                return True

        return False
