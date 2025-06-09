# Problem: 88. Merge Sorted Array
# Link: https://leetcode.com/problems/merge-sorted-array/
# Pattern: Two Pointers
# Topic: Array, Two Pointers, Sorting
# Difficulty: Easy
# Time: O(m + n) - Each element from nums1 and nums2 is compared and placed exactly once.
# Space: O(1) - The merge is performed in-place, using only a fixed amount of extra space for pointers.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None. Do not return anything, modify nums1 in-place instead.
        """

        # Step 1: Set up pointers at the end of the valid parts of nums1 and nums2
        pointer1 = m - 1            # Points to the last valid element in nums1
        pointer2 = n - 1            # Points to the last element in nums2
        pointer3 = m + n - 1        # Points to the last index in nums1

        # Step 2: Compare elements from the end, inserting the larger one at the current position in nums1
        while pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] > nums2[pointer2]:
                nums1[pointer3] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[pointer3] = nums2[pointer2]
                pointer2 -= 1
            pointer3 -= 1

        # Step 3: If any elements are left in nums2, copy them into nums1
        while pointer2 >= 0:
            nums1[pointer3] = nums2[pointer2]
            pointer2 -= 1
            pointer3 -= 1

# Example usage:
# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3
# Solution().merge(nums1, m, nums2, n)
# print(nums1)  # Output: [1, 2, 2, 3, 5, 6]