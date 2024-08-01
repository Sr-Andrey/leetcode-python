"""You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification."""

"""Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1."""

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def find_mountain_peak(self) -> int:
        left = 1
        right = self.arr_len - 2

        while left <= right:
            mid = left + (right - left) // 2
            val_left = self.arr.get(mid - 1)
            val_mid = self.arr.get(mid)
            val_right = self.arr.get(mid + 1)
            if val_left < val_mid < val_right:
                left = mid + 1
            elif val_left > val_mid > val_right:
                right = mid - 1
            else:
                return mid

    def bin_search(self, start: int, end: int, asc=True) -> int:
        """
        asc = True
        # sorted ascending: [1, 3, 6, ...]

        asc = False => desc = True
        # sorted descending: [7, 4, 2, ...]
        """
        left = start
        right = end

        while left <= right:
            mid = left + (right - left) // 2
            mid_value = self.arr.get(mid)
            if mid_value == self.target:
                return mid

            if mid_value > self.target:
                if asc:
                    right = mid - 1
                else:
                    left = mid + 1
            elif mid_value < self.target:
                if asc:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # equals
                return mid

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        self.arr = mountain_arr
        self.arr_len = self.arr.length()
        self.target = target
        peak = self.find_mountain_peak()
        if peak is None:
            return -1

        result = self.bin_search(0, peak, asc=True)
        if result is not None:
            return result

        result = self.bin_search(peak, self.arr_len - 1, asc=False)
        if result is not None:
            return result

        return -1
