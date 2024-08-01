"""Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order."""

"""Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109"""

class Solution:
    def two_sum(self, start: int, target: int) -> None:
        nums = self.nums
        left = start
        right = len(nums) - 1

        while left < right:
            left_value = nums[left]
            right_value = nums[right]
            val = left_value + right_value
            if val < target:
                left += 1
            elif val > target:
                right -= 1
            else:
                self.results.append(self.prefix + [left_value, right_value])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    def k_sum(self, k: int, start: int, target: int) -> None:
        if k == 2:
            self.two_sum(start, target)
            return

        nums = self.nums
        for idx in range(start, len(nums) - k + 1):
            if (
                # not start
                idx > start
                and
                # not same as prev
                nums[idx] == nums[idx - 1]
            ):
                continue
            value = nums[idx]
            self.prefix.append(value)
            self.k_sum(k - 1, idx + 1, target - value)
            self.prefix.pop()

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.nums = nums
        self.prefix = []
        self.results = []
        self.k_sum(4, 0, target)
        return self.results
