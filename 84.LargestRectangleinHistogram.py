"""Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram."""
"""Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4


Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for index, height in enumerate(heights):
            start = index
            while start and stack[-1][1]> height:
                prev_index, prev_height = stack.pop()
                max_area = max(max_area, prev_height*(index - prev_index))
                start = prev_index
            stack.append((start, height))

        for index, height in stack:
            max_area = max(max_area, height*(len(heights) - index))

        return max_area
