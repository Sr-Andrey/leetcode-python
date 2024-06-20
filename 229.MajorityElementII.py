"""Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times."""
"""Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]


Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cache = {}

        for num in nums:
            cache[num] = cache.get(num, 0) + 1
            if len(cache) > 2:
                for num, count in list(cache.items()):
                    if count == 1:
                        cache.pop(num)
                    else:
                        cache[num] = count - 1

        third = len(nums) // 3
        res = []
        for num in cache:
            if nums.count(num) > third:
                res.append(num)
        return res
