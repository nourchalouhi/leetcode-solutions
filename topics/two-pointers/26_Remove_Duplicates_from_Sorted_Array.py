# Problem: 26. Remove Duplicates from Sorted Array
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Pattern: Two Pointers
# Topic: Array, Two Pointers
# Difficulty: Easy
# Time: O(n) - Each element is compared at most once.
# Space: O(1) - In-place algorithm with only constant extra space for pointers.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        leftIndex = 0  # The index where the next unique value will go

        # Iterate through the array starting from the second element
        for rightIndex in range(1, len(nums)):
            if nums[rightIndex] != nums[leftIndex]:
                # Found a new unique number
                leftIndex += 1
                nums[leftIndex] = nums[rightIndex]
            # If duplicate, do nothing

        # leftIndex + 1 gives the count of unique elements
        return leftIndex + 1