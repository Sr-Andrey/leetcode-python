"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n))."""

"""Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106"""
class Solution:
    max_val = 10**6 + 1
    min_val = -max_val

    def get_middle_vals(self, idx: int, nums: List[int]) -> Tuple[int, int]:
        max_left = nums[idx] if idx >= 0 else self.min_val
        next_idx = idx + 1
        min_right = nums[next_idx] if next_idx < len(nums) else self.max_val
        return max_left, min_right

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s1 = len(nums1)
        s2 = len(nums2)
        if s1 > s2:
            return self.findMedianSortedArrays(nums2, nums1)

        total = s1 + s2
        half, is_odd = divmod(total, 2)

        left = 0
        right = s1 - 1

        while True:
            idx1 = left + (right - left) // 2
            idx2 = half - idx1 - 2

            max_left_1, min_right_1 = self.get_middle_vals(idx1, nums1)
            max_left_2, min_right_2 = self.get_middle_vals(idx2, nums2)

            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                if is_odd:
                    return min(min_right_1, min_right_2)
                return (
                    min(min_right_1, min_right_2)
                    +
                    max(max_left_1, max_left_2)
                ) / 2

            if max_left_1 > min_right_2:
                right = idx1 - 1
            else:
                left = idx1 + 1
