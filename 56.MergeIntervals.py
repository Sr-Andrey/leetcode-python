"""Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input."""

"""Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key=lambda pair: pair[0])
        intervals.sort()
        output = [intervals[0]]

        # for start, end in intervals[1:]
        for idx in range(1, len(intervals)):
            start, end = intervals[idx]
            last_interval = output[-1]
            last_end = last_interval[1]

            if start > last_end:
                output.append(intervals[idx])
                # output.append([start, end])
            else:
                last_interval[1] = max(last_end, end)

        return output
